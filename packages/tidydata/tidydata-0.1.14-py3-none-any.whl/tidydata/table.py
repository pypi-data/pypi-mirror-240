import pandas as pd
import numpy as np
from typeguard import typechecked
from typing import (
    Dict,
    Optional,
    Literal,
    Union,
    Any,
    Sequence,
    Set,
    Callable,
    List,
    Tuple,
)
from pathlib import Path
from pandas.io.stata import StataReader, StataWriter
from pandas.api.types import (
    is_numeric_dtype,
    is_datetime64_any_dtype,
    is_integer_dtype,
    is_string_dtype,
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_object_dtype,
    is_scalar,
    infer_dtype
)

from pandas._libs.missing import NAType
from ast import literal_eval

Intervalable = Union[int, float, pd.Timestamp]
numpy_numeric_dtypes = {
    "int8": np.int8,
    "int16": np.int16,
    "int32": np.int32,
    "int64": np.int64,
    "uint8": np.uint8,
    "uint16": np.uint16,
    "uint32": np.uint32,
    "uint64": np.uint64,
    "float16": np.float16,
    "float32": np.float32,
    "float64": np.float64,
    "complex64": np.complex64,
    "complex128": np.complex128,
}


def is_np_numeric_dtype(dtype):
    dtype_alias = dtype.name
    if dtype_alias in numpy_numeric_dtypes.keys():
        return True
    else:
        return False


def is_np_string_dtype(dtype):
    if dtype.name == "object" and is_string_dtype(dtype):
        return True
    else:
        return False


user_dtype_aliases = {
    "Int": "Int64",
    "int": "int64",
    "UInt": "UInt64",
    "uint": "uint64",
    "str": "str",
    "Str": "string",
    "Float": "Float64",
    "float": "float64",
    "Bool": "boolean",
    "cat": "category",
    "Cat": "category",
    "date": "datetime64[ns]",
    "Date": "datetime64[ns, UTC]",
    "Timed": "timedelta64[ns]",
    "timed": "timedelta64[ns]",
    "Obj": "object",
    "obj": "object"
}

infer_dtype_aliases ={
    'string': 'str',
    'bytes': 'int',
    'floating': 'float',
    'integer': 'int',
    'decimal': 'float',
    'complex': 'complex',
    'categorical': 'cat',
    'boolean': 'bool',
    'datetime64': 'date',
    'timedelta64': 'timed',
    'timedelta': 'obj',
    'datetime' : 'obj',
    'mixed-integer': 'obj',
    'mixed-integer-float': 'obj',
    'date': 'obj',
    'time': 'obj',
    'period': 'period',
    'mixed': 'obj',
    'unknown-array': 'obj'
}

@typechecked
def to_flatten_index(multi_index: pd.MultiIndex, flat_sep="_"):
    """合并多重索引到单层"""
    return [flat_sep.join(map(str, col)).strip() for col in multi_index]


@typechecked
class Column(pd.Series):
    # 临时属性
    _internal_names = pd.Series._internal_names
    _internal_names_set = set(_internal_names)
    # 永久属性
    _metadata = ["label"]

    @property
    def _constructor(self):
        return Column

    @property
    def _constructor_expanddim(self):
        return Table

    def __init__(self, data=None, *args, label: Optional[str] = None, **kwargs):
        super().__init__(data, *args, **kwargs)
        self.label = label

    def nasum(self, *args):
        df = pd.DataFrame([self] + list(args))  # 在eval中只能生成df后计算而不能使用Table计算
        column = df.sum(skipna=True).mask(df.isna().all()).convert_dtypes()
        return Column(column)

    def namean(self, *args):
        df = pd.DataFrame([self] + list(args))  # 在eval中只能生成df后计算而不能使用Table计算
        column = df.mean(skipna=True).mask(df.isna().all()).convert_dtypes()
        return Column(column)

    def strcat(self, *args, sep: str = "", na: Optional[str] = None):
        """Concatenate column with others"""
        column = self.astype("string")

        for arg in args:
            if is_scalar(arg):
                arg = Column(arg, index=self.index, dtype="string")
            column = column.str.cat(arg.astype("string"), na_rep=na, sep=sep)
        return column

    def strins(self, s, loc: int, na: Optional[str] = None):
        """Insert string in column at specific location"""

        column = self.astype("string")
        if na is not None:
            column.fillna(na, inplace=True)
        column = column.str.slice(0, loc) + str(s) + column.str.slice(loc)
        return column


@typechecked
class Table(pd.DataFrame):
    """Table继承pd.DataFrame"""

    # 临时属性
    _internal_names = pd.DataFrame._internal_names
    _internal_names_set = set(_internal_names)
    # 永久属性
    _metadata = ["_name", "_description", "_column_labels"]

    @property
    def _constructor(self):
        return Table

    @property
    def _constructor_sliced(self):
        return Column

    def __init__(
        self,
        data=None,
        *args,
        name: str = "unnamed_table",
        description: str = "",
        column_labels: Optional[Dict[str, str]] = None,
        **kwargs,
    ):

        super().__init__(data, *args, **kwargs)
        self.flags.allows_duplicate_labels = False  # 保证
        self._normalize_column_names()
        self._name = name
        self._description = description
        self._column_labels = Column(self.columns.to_series())
        if column_labels is not None:
            self._column_labels.update(column_labels)

    def _normalize_column_names(self):
        if self.columns.hasnans:
            raise IndexError(f"Column names can not contain NA value")
        if isinstance(self.columns, pd.MultiIndex):
            self.columns = to_flatten_index(self.columns)
        else:
            self.columns = self.columns.astype(str).str.strip()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value: str):
        self._description = value

    @property
    def column_labels(self):
        return self._column_labels.reindex(self.columns)

    @column_labels.setter
    def column_labels(self, value: Dict[str, str]):
        new_labels = Column(value).reindex(self.columns).astype("string")
        self._column_labels = new_labels.combine_first(self._column_labels)

    @property
    def column_dtypes(self):
        df =pd.DataFrame.from_records({name: [infer_dtype(col,skipna=True), col.hasnans] for name, col in self.items()}).T.astype({1:'bool'})
        df.rename(columns={0:'dtype',1:'hasna'}, inplace=True)
        df.replace({'dtype':infer_dtype_aliases}, inplace=True)
        
        return df['dtype'].mask(df['hasna'], df['dtype'].str.capitalize())
        # dtypes = self.dtypes
        # np_str_dtypes = dtypes.where(dtypes.map(is_np_string_dtype)).replace(
        #     {"object": "str"}
        # )
        # dtype_to_aliases = {raw: alias for alias, raw in user_dtype_aliases.items()}
        # other_dtypes = dtypes.astype(str).replace(dtype_to_aliases)
        # return np_str_dtypes.combine_first(other_dtypes)

    @column_dtypes.setter
    def column_dtypes(self, value: Dict[str, str]):
        self = self.convert_column_dtypes(value, copy=False)

    def _update_info(self, **kwargs):
        name = kwargs.get("name")
        description = kwargs.get("description")
        column_labels = kwargs.get("column_labels")
        column_dtypes = kwargs.get("column_dtypes")

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if column_labels is not None:
            self.column_labels = column_labels
        if column_dtypes is not None:
            self.column_dtypes = column_dtypes

    # 获取列的值区间
    @property
    def column_value_ranges(self):
        pass

    # 获取表的描述性统计

    def describe_columns(
        self, include_dtypes: Optional[str | List[str]] = None, empty: bool = True
    ):
        if self.empty and not empty:
            return self

        name = f"Column_info: {self.name}"
        description = f"Column_info: {self.description}"
        column_labels = {
            "name": "Column name",
            "label": "Column label",
            "dtype": "Column dtype",
            "value_range": "Column value range",
        }
        data = {
            "name": self.columns,
            "label": self.column_labels,
            "dtype": self.column_dtypes,
            "value_range": pd.NA,
        }
        table = Table(
            data, name=name, description=description, column_labels=column_labels
        ).reset_index(drop=True)
        return table

    def convert_column_dtypes(
        self, dtypes: Optional[Dict[str, str]] = None, copy: bool = True
    ):
        """Convert columns' data types"""

        if dtypes is None:
            return self

        table = self.copy(deep=True) if copy else self
        for col, dtype in dtypes.items():
            to_dtype = user_dtype_aliases.get(dtype) or dtype
            
            table[col] = (
                table[col]
                .convert_dtypes(dtype_backend="numpy_nullable")
                .astype(to_dtype, copy=False)
            )

        return table

    def replace_column_values(
        self,
        values: Dict[str, Dict],
        copy: bool = True,
        na_alias: str = "NA",
        regex: bool = False,
        literal_eval: bool = False,
        **kwargs,
    ):
        """Replace columns' values to new values"""
        table = self.copy(deep=True) if copy else self

        if literal_eval:
            values = Column(values).map(literal_eval).to_dict()

        fillnas = {
            col: new_value
            for col, value_map in values.items()
            for value, new_value in value_map.items()
            if isinstance(value, NAType) or value == na_alias
        }

        for col, value in fillnas.items():
            table[col] = table[col].fillna(value)

        table.replace(values, regex=regex, inplace=True)
        table._update_info(**kwargs)

        return table

    def limit_column_values(
        self,
        limits: Dict[str, str | List | Tuple[Intervalable, Intervalable]],
        copy: bool = True,
        literal_eval: bool = False,
        catcols: Optional[List[str]] = None,
        errors: Literal["raise", "coerce"] = "raise",
        **kwargs,
    ):
        """Set value range of columns"""
        table = self.copy(deep=True) if copy else self
        if literal_eval:
            limits = Column(limits).map(literal_eval).to_dict()

        for col, limit in limits.items():
            s = table[col]
            original_dtype = s.dtype
            if isinstance(limit, List):
                if isinstance(original_dtype, pd.CategoricalDtype) or s.name in catcols:
                    cats = pd.CategoricalDtype(limit, ordered=True)
                    table[col] = s.astype(cats)
                else:
                    table[col] = s.where(s.isin(limit))
            else:
                if not (
                    is_datetime64_any_dtype(original_dtype)
                    or is_numeric_dtype(original_dtype)
                ):
                    if errors == "coerce":
                        s = (
                            pd.to_numeric(s, errors="coerce")
                            if not is_datetime64_any_dtype(original_dtype)
                            else pd.to_datetime(s, errors="coerce")
                        )
                    else:
                        raise TypeError(
                            f"Unsupported dtype: tuple limits only support numeric or datetime dtypes, other dtypes use list limit instead"
                        )
                table[col] = s.where(s.between(limit[0], limit[1], inclusive="both"))

        table._update_info(**kwargs)
        return table

    def rename_columns(self, names: Dict[str, str], copy: bool = True, **kwargs):
        table = self.copy(deep=True) if copy else self
        new_labels = {v: table.column_labels[k] for k, v in names.items()}

        table = table.rename(columns=names, errors="raise")
        table.column_labels = new_labels
        table._update_info(**kwargs)

        return table

    def as_pandas_df(self, copy: bool = True):
        return pd.DataFrame(self, copy=copy)

    def lreshape_table(
        self,
        stubnames: List[str] | str,
        i: List[str] | str,
        j: str,
        sep: str = "@",
        suffix: str = r".+",
        prenames: Optional[Dict[str, str]] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        column_labels: Optional[Dict[str,str]] = None,
        column_dtypes: Optional[Dict[str,str]] = None
    ):
        """Reshape table to long format"""
        
        df = self.as_pandas_df(copy=True)

        if prenames is not None:
            df.rename(columns=prenames, inplace=True)

        df = pd.wide_to_long(df, stubnames=stubnames, i=i, j=j, sep=sep, suffix=suffix)
        df.reset_index(inplace=True)
        df = df.astype({f"{j}": "str"}, copy=False)
        table = self.__class__(
            df,
            name=(name or self.name),
            description=(description or self.description),
            column_labels=(column_labels or self.column_labels),
            copy=False,
        )
        if column_dtypes is not None:
            table.column_dtypes = column_dtypes
        return table

    def select_columns(self, usecols: List[str] | str | pd.Index, copy: bool = True):
        """Select columns subset"""
        table = self.copy(deep=True) if copy else self
        table = table[usecols]
        return table

    def select_rows(self, userows: str | List, copy: bool = True):
        """Select rows subset"""
        table = self.copy(deep=True) if copy else self

        if isinstance(userows, str):
            table.query(userows, inplace=True)

        elif isinstance(userows, list) and is_integer_dtype(pd.Index(userows).dtype):
            table = table.iloc[userows]
        else:
            table = table.loc[userows]
        return table

    def mutate_columns(
        self, 
        exprs: Dict[str, str], 
        copy: bool = False, 
        name: Optional[str] = None,
        description: Optional[str] = None,
        column_labels: Optional[Dict[str,str]] = None,
        column_dtypes: Optional[Dict[str,str]] = None
    ):
        """Mutate columns by evaluating the existing columns"""

        table = self.copy(deep=True) if copy else self
        eval_str = "\n".join([rf"{key} = {value}" for key, value in exprs.items()])
        table.eval(eval_str, inplace=True)
        if name is not None:
            table.name = name
        if description is not None:
            table.description = description
        if column_labels is not None:
            table.column_labels = column_labels
        if column_dtypes is not None:
            table.column_dtypes = column_dtypes

        return table

    def append_tables(
        self,
        other_tables: List["Table"] | "Table" ,
        on: Optional[List[str] | str] = None,
        drop_duplicates: bool = True,
        ignore_index: bool = True,
        name: Optional[str] = None,
        description: Optional[str] = None,
        column_labels: Optional[Dict[str,str]] = None,
        column_dtypes: Optional[Dict[str,str]] = None
    ):
        """Union observations with other tables"""

        use_tables = (
            [self] + other_tables
            if isinstance(other_tables, list)
            else [self] + [other_tables]
        )
        table = pd.concat(
            use_tables, axis=0, join="outer", copy=False, ignore_index=ignore_index
        )

        if drop_duplicates:
            table.drop_duplicates(inplace=True)
        if on is not None:
            table.select_columns(on)

        union_labels = self.column_labels
        for other_table in other_tables:
            union_labels = union_labels.combine_first(other_table.column_labels)
        table.column_labels = union_labels.to_dict()
        
        if name is not None:
            table.name = name
        if description is not None:
            table.description = description
        if column_labels is not None:
            table.column_labels = column_labels
        if column_dtypes is not None:
            table.column_dtypes = column_dtypes

        return table

    def merge_tables(
        self,
        other_tables: List["Table"] | "Table",
        on: str | List[str],
        how: Literal["left", "right", "inner", "outer"] = "left",
        mode: Optional[str] = None,
        indicator: bool = False,
        sort: bool = False,
        name: Optional[str] = None,
        description: Optional[str] = None,
        column_labels: Optional[Dict[str,str]] = None,
        column_dtypes: Optional[Dict[str,str]] = None
    ):
        """Match observations' columns by specific column names from left to right"""

        other_tables = (
            [other_tables] if isinstance(other_tables, Table) else other_tables
        )
        modes = (
            [s for s in mode.strip().split(":") if s in ("1", "m")]
            if mode is not None
            else ["m"] * (len(other_tables) + 1)
        )
        if len(modes) != len(other_tables) + 1:
            raise ValueError(
                f"Invalid mode format: Use colons to separate values with '1' or 'm' on either side. Colon count should match 'other_tables'."
            )

        table = self.copy(deep=True)
        on = [on] if isinstance(on, str) else on

        if modes[0] == "1":
            if table[on].duplicated().any():
                raise ValueError(
                    f"Invalid match ID: column {on} in self table is not unique"
                )

        union_labels = self.column_labels
        for i, other_table in enumerate(other_tables, start=1):
            if modes[i] == "1":
                if other_table[on].duplicated().any():
                    raise ValueError(
                        f"Invalid match ID: column {on} in table {i} is not unique"
                    )
            table = table.merge(
                right=other_table,
                on=on,
                how=how,
                copy=False,
                indicator=indicator,
                sort=sort,
            )

            union_labels = union_labels.combine_first(other_table.column_labels)

        table.column_labels = union_labels.to_dict()
        if name is not None:
            table.name = name
        if description is not None:
            table.description = description
        if column_labels is not None:
            table.column_labels = column_labels
        if column_dtypes is not None:
            table.column_dtypes = column_dtypes
        return table

    # 统一格式为numpy类型
    def convert_dtype_backend(
        self,
        backend: Literal["numpy", "numpy_nullable", "pyarrow"] = "numpy",
        copy: bool = True,
    ):
        table = self.copy() if copy else self

        if backend == "pyarrow":
            table = table.convert_dtypes(dtype_backend=backend)

        elif backend == "numpy_nullable":
            table = table.convert_dtypes(dtype_backend=backend)
            for col, dtype in table.dtypes.items():
                if is_datetime64_any_dtype(dtype):
                    table[col] = table[col].astype("datetime64[ns, UTC]")
            # 转换时间为timestamp类型
        else:
            # 转换pd.NA为
            for col, dtype in table.dtypes.items():
                if is_datetime64_any_dtype(dtype):
                    table[col] = table[col].astype("datetime64[ns]")
                elif isinstance(dtype, pd.CategoricalDtype):
                    pass
                elif is_string_dtype(dtype):
                    table[col] = table[col].astype("object").fillna(np.nan)
                else:
                    if table[col].hasnans:
                        table[col] = table[col].astype("object").fillna(np.nan)

        return table


    @classmethod
    def from_pickle(
        cls,
        file: Optional[str | Path] = None,
        usecols: Optional[List[str]] = None,
        name: str = "unnamed_table",
        description: str = "",
    ):
        """Create table from pickle file"""
        if file is None:
            return cls(name=name, description=description)

        data = pd.read_pickle(file)
        if usecols is not None:
            data = data[usecols]

        table = data if isinstance(data, Table) else cls(data)
        return table

    @classmethod
    def from_pkl(cls, *arg, **kwargs):
        return cls.from_pickle(*arg, **kwargs)

    def to_dta(
        self,
        file: str | Path,
        index: bool = False,
    ):
        file = Path(file)
        table = self._set_inf_as_na().convert_dtype_backend("numpy")
        data_label = table.description if table.description is not None else ""
        variable_labels = table.column_labels.dropna().to_dict()
        table.to_stata(
            path=file,
            write_index=index,
            version=118,
            data_label=data_label,
            variable_labels=variable_labels,
        )
        #table.describe_columns.to_csv(file.with_suffix(".csv"))

    def _set_inf_as_na(self, copy: bool = True):
        table = self.copy(deep=True) if copy else self
        table.replace([np.inf, -np.inf], np.nan, inplace=True)
        return table

    # 替换StataMissingValue为任意值
    def replace_stata_na(self, values: Dict[str, Any] | Any):
        pass



