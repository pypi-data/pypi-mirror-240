from pydantic import BaseModel, field_validator, model_validator, create_model
from datetime import datetime
from typing import Optional, List, Literal, Dict, Any, Tuple, Union, Callable
from pathlib import Path
import pandas as pd
import pandera as pa
from pandera import DataFrameSchema, Check, Column
import yaml
import toml
from tidydata.table import user_dtype_aliases
from ast import literal_eval
from pandas._libs.missing import NAType
from loguru import logger
from tidydata.table import Table
import inspect
import re
from tidydata.table import user_dtype_aliases
from tidydata.io import table_readers
import shutil

    
    

dtype_aliases = list(user_dtype_aliases.keys())

table_pipes = {
    k: v
    for k, v in vars(Table).items()
    if not k.startswith("__")
    and not k.startswith("_")
    and not k.startswith("to")
    and inspect.isfunction(v)
}

table_writers = {
    k: v for k, v in vars(Table).items() if k.startswith("to") and inspect.isfunction(v)
}


is_nullable_range_column = Check(
    lambda s: (
        lambda eval_s: True
        if (isinstance(eval_s, tuple) and len(eval_s) == 2) or isinstance(eval_s, list)
        else False
    )(literal_eval(s))
    if not isinstance(s, NAType)
    else True,
    element_wise=True,
    error="Non_nullable string value can not been parsed as range (list or tuple)",
)

is_nullable_dict_column = Check(
    lambda x: isinstance(literal_eval(x), dict) if not isinstance(x, NAType) else True,
    element_wise=True,
    error="Non_nullable string value can not been parsed as dict",
)

is_nullable_unique_column = Check(
    lambda s: s.duplicated() == False, error=f"Non-nullable string is not unique"
)
isin_nullable_column = lambda values: Check(
    lambda x: x in values if not isinstance(x, NAType) else True,
    element_wise=True,
    error="Non_nullable string values are all in {values}",
)


def create_model_from_function(
    func: Callable, 
    name: Optional[str] =None):
    """Create pydantic model from function or instance method"""
    
    model_name= name or f"{func.__name__.capitalize()}FunctionModel"
    par_info = dict(inspect.signature(func).parameters)
    
    for field in ['self','copy']:
        if par_info.get(field) is not None:
            par_info.pop(field)
    
    model_fields = {name: (value.annotation, value.default) if value.default is not inspect._empty else (value.annotation, ...)
        for name, value in par_info.items()
    }
    
    return create_model(model_name, __config__={'extra':'forbid'}, **model_fields)


## 设置ColumnMeta模板
colmeta_schema = DataFrameSchema(
    {
        "name": Column(str, unique=True),
        "label": Column(str, unique=True),
        "dtype": Column(str, checks=Check(lambda s: s.isin(user_dtype_aliases))),
        "alias": Column(str, nullable=True, checks=is_nullable_unique_column),
        "value_range": Column(str, nullable=True, checks=is_nullable_range_column),
        "value_premap": Column(str, nullable=True, checks=is_nullable_dict_column),
    }
)






class ColumnMeta(BaseModel):
    names: List[str]
    labels: Dict[str, str]
    aliases: Dict[str, str]
    dtypes: Dict[str, str]
    value_ranges: Dict[
        str, Tuple[int | float | datetime, int | float | datetime] | List
    ]
    value_premaps: Dict[str, Dict]
    catcols: List[str]

    @classmethod
    def from_csv(cls, file: str | Path):
        usecols = [
            "name",
            "label",
            "alias",
            "dtype",
            "value_range",
            "value_premap",
            "is_use",
        ]
        df = colmeta_schema.validate(
            pd.read_csv(file, dtype="string", usecols=usecols)
            .transform(lambda s: s.str.strip())
            .query("is_use=='1'")
            .drop(columns="is_use")
        )

        for col in ["value_range", "value_premap"]:
            df[col] = df[col].map(literal_eval, na_action="ignore")

        df.set_index("name", inplace=True)

        colmeta = {
            "names": df.index.to_list(),
            "labels": df["label"].to_dict(),
            "dtypes": df["dtype"].to_dict(),
            "aliases": df["alias"].dropna().to_dict(),
            "value_ranges": df["value_range"].dropna().to_dict(),
            "value_premaps": df["value_premap"].dropna().to_dict(),
            "catcols": df.query("dtype.isin(['cat'])").index.to_list(),
        }
        return cls(**colmeta)


class SourceMeta(BaseModel):
    """Source元信息类"""

    name: str
    file: str
    colmeta: str | ColumnMeta
    description: str = ""
    docs: str = ""
    opts: Literal["default"] | Dict[str, Any] = "default"

    # 检查name：只允许数字字母下划线
    @field_validator("name")
    def check_name(cls, name):
        logger.info(f"Validating name in source metadata...")
        pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
        if not re.match(pattern, name):
            raise logger.error(
                f"{name} is a string that start with a letter or the underscore character, and only contain alpha-numeric characters and underscores"
            )
        return name

    @field_validator("colmeta")
    def check_column(cls, colmeta):
        if isinstance(colmeta, str):
            colmeta = Path(colmeta).resolve()
            logger.info(f"Validating colmeta in source metadata: {colmeta}...")
            if colmeta.suffix != ".csv":
                raise logger.error(f"Column meta path {colmeta} is not a csv file")

            return ColumnMeta.from_csv(colmeta)
        return colmeta

    @model_validator(mode="after")
    def check_reader(self):
        logger.info(f"Validating source {self.name}...")
        file = Path(self.file).resolve()

        reader = table_readers.get(file.suffix)
        if reader is None:
            raise logger.error(
                f"Source '{self.name}' can not find not appropriate reader as its data suffix is not in {list(table_readers.keys())}"
            )

        if self.opts != "default":
            try:
                reader = reader.model_validate(self.opts)
            except Exception as e:
                raise logger.error(
                    f"Reader for the source '{self.name}' has inappropriate options: {e}"
                )

        self.opts = reader

    @property
    def data(self):
        return (
            self.opts.read(
                file=self.file,
                usecols=self.colmeta.names,
                name=self.name,
                description=self.description,
                column_labels=self.colmeta.labels,
            )
            .replace_column_values(self.colmeta.value_premaps, copy=False)
            .limit_column_values(
                self.colmeta.value_ranges, catcols=self.colmeta.catcols, copy=False
            )
            .convert_column_dtypes(self.colmeta.dtypes, copy=False)
            .rename_columns(self.colmeta.aliases, copy=False)
        )



class ActionMeta(BaseModel):
    """Data模块"""
    name: str
    source: str
    pipes: List[Dict[str, Any]]
    description: str = ""
    export: bool = True

    @field_validator("name")
    def check_name(cls, name):
        logger.info(f"Validating name in action metadata...")
        pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
        if not re.match(pattern, name):
            raise logger.error(
                f"{name} is a string that starts with a letter or the underscore character, and only contains alpha-numeric characters and underscores"
            )
        return name
    
    # @model_validator(mode='after')
    # def check_pipes(self):

    #     table_funcs = []
    #     for pipe in self.pipes:
    #         func = pipe['func']
    #         kwargs = pipe['kwargs']
    #         func = table_pipes.get(func)
    #         if func is None:
    #             raise logger.error(f"Can not find supported pipe function for '{func}'")
            
    #         create_model_from_function(func).model_validate(kwargs)
            
    #         table_funcs.append((func, kwargs))
            
    #     self.pipes = table_funcs
        

    def apply_pipes(self, table:Table):
        """apply table function to a Table"""
        for func, kwargs in self.pipes:
            table = table.pipe(func, **kwargs)
        return table
            


class AuthorMeta(BaseModel):
    """Author元信息类"""

    name: str = "kyrie"
    email: str = "kyrie1218@xx.com"
    github: str = "kyrie1218"
    affiliation: str = "XX University"


class ProjectMeta(BaseModel, extra='forbid'):
    """Project元信息类"""

    name: str = "unnamed_project"
    description: str = "Describe your project here..."
    authors: List[AuthorMeta] = [AuthorMeta()]
    date: datetime | str = datetime.now().date()
    date_modified: datetime | str = datetime.now().date()
    sources: str = "sources.yaml"
    actions: str = "actions.yaml"
    export_dir: str | Path = Path('cleaned/').resolve()


    @model_validator(mode='after')
    def check_sources(self):
        """Check and transform sources to a dictionary of SourceMeta"""
        source_path = Path(self.sources).resolve()

        if source_path.suffix not in [".yaml", ".yml"] or not source_path.is_file():
            raise logger.error(f"file {source_path} is not a existing yaml file")

        with open(source_path, "rb") as f:
            source_dict = yaml.safe_load(f)

        if source_dict is None:
            raise logger.error(
                f"Parsed dictionary from yaml file {source_path} is empty"
            )

        source_list = source_dict.get("sources")
        if source_list is None:
            raise logger.error(
                f"source dictionary from yaml file {source_path} does not have the 'sources' key"
            )
        if not isinstance(source_list, list):
            raise logger.error(
                f"Value of the 'sources' key is not a list in yaml file {source_path}"
            )

        sourcebase = {src["name"]: SourceMeta(**src) for src in source_list}
        logger.info(f"Checking the uniqueness of names in sources...")
        if len(sourcebase) != len(source_list):
            raise logger.error(
                f"name in sources from yaml file {source_path} is not unique"
            )
        self.sources = sourcebase

        """Check and transform actions to a dictionary of ActionMeta"""

        action_path = Path(self.actions).resolve()
        if action_path.suffix not in [".yaml", ".yml"] or not action_path.is_file():
            raise logger.error(f"file {action_path} is not a existing yaml file")
        logger.info(f"Loading yaml file {action_path} to a dictionary")
        with open(action_path, "rb") as f:
            action_dict = yaml.safe_load(f)
        logger.info(f"Indexing the actions key...")
        action_list = action_dict.get("actions")
        if action_list is None:
            raise logger.error(
                f"yaml file {action_path} does not have the 'actions' key"
            )

        if not isinstance(action_list, list):
            raise logger.error(
                f"Value of the 'actions' key is not a list in yaml file {action_path}"
            )

        logger.info(f"Creating the dictionary of ActionMeta object...")
        
        
        actionbase = {action["name"]: ActionMeta(**action) for action in action_list}
        logger.info(f"Checking the uniqueness of names in actions...")
        if len(actionbase) != len(action_list):
            raise logger.error(
                f"name in actions from yaml file {action_path} is not unique"
            )
            
        self.actions = actionbase
    
    

    def run(self):
        logger.info(f"==> Creating cache directory '_cache_files' in current directory")
        cache_dir = Path("_cache_files")

        cache_src_dir = (cache_dir / 'sources').resolve()
        cache_src_dir.mkdir(parents=True, exist_ok=True)
        cache_pipe_dir = (cache_dir / 'pipes').resolve()
        cache_pipe_dir.mkdir(parents=True, exist_ok=True)
        
        cache_files = {}
        for name, src in self.sources.items():
            cache_src_file = cache_src_dir / f"{name}.pickle"
            src.data.to_pickle(cache_src_file)
            cache_files[name] = cache_src_file
            
 
        for name, action in self.actions.items():
            
            cache_pipe_file = cache_pipe_dir / f"{name}.pickle"
            
            table = pd.read_pickle(cache_files[action.source])
            for kwargs in action.pipes:
                func_name = kwargs.pop('func')
                func = table_pipes[func_name]
                if func_name in ['append_tables','merge_tables']:
                    other_tables = [pd.read_pickle(cache_files[table_name]) for table_name in kwargs['other_tables']]
                    kwargs.update({'other_tables':other_tables})
                    
                #create_model_from_function(func).model_validate(kwargs)
                    
                table = table.pipe(func, **kwargs)
            
            if action.export:
                
                file = self.export_dir / f"{name}.dta"
                logger.info(f"Exporting table '{name}' to '{file}'")
                table.to_dta(file)
  
            table.to_pickle(cache_pipe_file)
            cache_files[name] = cache_pipe_file
        
        shutil.rmtree(cache_dir)
    @classmethod
    def from_toml(cls, file: str | Path):
        """Create config object from toml file"""
        file_path = Path(file).resolve()
        logger.info(f"Loading project configuration from file {file_path}")

        if file_path.suffix not in [".toml"]:
            raise logger.error(f"file {file_path} is not a toml file")

        logger.info("Creating config object from toml file")
        conf = toml.load(file_path)

        return cls(**conf['project'])
        
    

        
        
