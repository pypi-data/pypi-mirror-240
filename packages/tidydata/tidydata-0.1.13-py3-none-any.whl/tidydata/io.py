import pandas as pd
from pathlib import Path
from typing import List, Optional, Literal, Dict
from tidydata.table import Table
from loguru import logger
from typeguard import typechecked
from pydantic import BaseModel
import numpy as np

@typechecked
def read_stata(
    file: str | Path,
    usecols: Optional[List[str]] = None,
    name: str = "unnamed_table",
    description: str = "",
    column_labels: Optional[Dict[str, str]] = None,
    to_categoricals: bool = False,
    to_stataNAs: bool = False,
    to_datetimes: bool = True,
) -> Table:
    """Read stata file as pandas DataFrame object: any stata missing will be as NA"""

    file = Path(file).resolve()
    if file.suffix != ".dta":
        raise logger.error(f"file {file} is not a stata file with suffix '.dta'")

    df = pd.read_stata(
        file,
        columns=usecols,
        convert_categoricals=to_categoricals,
        order_categoricals=to_categoricals,
        convert_missing=to_stataNAs,
        convert_dates=to_datetimes,
    )
    with pd.io.stata.StataReader(file) as meta:
        raw_description = meta.data_label
        raw_column_labels = pd.Series(meta.variable_labels())

    description = raw_description or description
    if column_labels is not None:
        raw_column_labels.update(column_labels)

    return Table(
        data=df,
        name=name,
        description=description,
        column_labels=raw_column_labels.to_dict(),
        copy=False,
    )


@typechecked
def read_csv(
    file: str | Path,
    usecols: Optional[List[str]] = None,
    name: str = "unnamed_table",
    description: str = "",
    column_labels: Optional[Dict[str, str]] = None,
    dtype: Optional[str | Dict[str, str]] = None,
    sep: str = ",",
    encoding: str = "utf-8",
) -> Table:
    """Read csv file as a Table"""

    df = pd.read_csv(file, usecols=usecols, dtype=dtype, sep=sep, encoding=encoding)
    return Table(
        data=df,
        name=name,
        description=description,
        column_labels=column_labels,
        copy=False,
    )


@typechecked
def read_excel(
    file: str | Path,
    usecols: Optional[List[str]] = None,
    name: str = "unnamed_table",
    description: str = "",
    column_labels: Optional[Dict[str, str]] = None,
    dtype: Optional[str | Dict[str, str]] = None,
    sheet: str | int = 0,
) -> Table:
    """Read excel file as a Table"""

    df = pd.read_excel(file, usecols=usecols, dtype=dtype, sheet_name=sheet)
    return Table(
        data=df,
        name=name,
        description=description,
        column_labels=column_labels,
        copy=False,
    )


@typechecked
def read_parquet(
    file: str | Path,
    usecols: Optional[List[str]] = None,
    name: str = "unnamed_table",
    description: str = "",
    column_labels: Optional[Dict[str, str]] = None,
    engine: Literal["auto", "pyarrow", "fastparquet"] = "auto",
) -> Table:
    """Read parquet file as a Table"""
    df = pd.read_parquet(file, columns=usecols, engine=engine)
    return Table(
        data=df,
        name=name,
        description=description,
        column_labels=column_labels,
        copy=False,
    )


class StataReader(BaseModel, extra="forbid"):
    """StataReader类"""

    to_categoricals: bool = False
    to_stataNAs: bool = False
    to_datetimes: bool = True

    def read(
        self,
        file: str | Path,
        usecols: Optional[List[str]] = None,
        name: str = "unnamed_table",
        description: str = "",
        column_labels: Optional[Dict[str, str]] = None,
    ) -> Table:
        return read_stata(
            file=file,
            usecols=usecols,
            name=name,
            description=description,
            column_labels=column_labels,
            to_categoricals=self.to_categoricals,
            to_stataNAs=self.to_stataNAs,
            to_datetimes=self.to_datetimes,
        )


class ExcelReader(BaseModel, extra="forbid"):
    """ExcelReader类"""

    dtype: Optional[str | Dict[str, str]] = None
    sheet: str | int = 0

    def read(
        self,
        file: str | Path,
        usecols: Optional[List[str]] = None,
        name: str = "unnamed_table",
        description: str = "",
        column_labels: Optional[Dict[str, str]] = None,
    ) -> Table:
        return read_excel(
            file=file,
            usecols=usecols,
            name=name,
            description=description,
            column_labels=column_labels,
            dtype=self.dtype,
            sheet=self.sheet,
        )


class CsvReader(BaseModel, extra="forbid"):
    """CsvReader类"""

    dtype: Optional[str | Dict[str, str]] = None
    sep: str = ","
    encoding: str = "utf-8"

    def read(
        self,
        file: str | Path,
        usecols: Optional[List[str]] = None,
        name: str = "unnamed_table",
        description: str = "",
        column_labels: Optional[Dict[str, str]] = None,
    ) -> Table:
        return read_csv(
            file=file,
            usecols=usecols,
            name=name,
            description=description,
            column_labels=column_labels,
            dtype=self.dtype,
            sep=self.sep,
            encoding=self.encoding,
        )


class ParquetReader(BaseModel, extra="forbid"):
    engine: Literal["auto", "pyarrow", "fastparquet"] = "auto"

    def read(
        self,
        file: str | Path,
        usecols: Optional[List[str]] = None,
        name: str = "unnamed_table",
        description: str = "",
        column_labels: Optional[Dict[str, str]] = None,
    ) -> Table:
        return read_parquet(
            file=file,
            usecols=usecols,
            name=name,
            description=description,
            column_labels=column_labels,
            engine=self.engine,
        )


table_readers = {
    ".csv": CsvReader(),
    ".tsv": CsvReader(),
    ".dta": StataReader(),
    ".xlsx": ExcelReader(),
    ".xls": ExcelReader(),
    ".pq": ParquetReader(),
    ".parquet": ParquetReader(),
}

# Table writer

# def to_stata(
#     table: Table, 
#     file: str | Path,
#     ignore_index: bool = True, 
#     export_metadata: bool = False):
#     """Write table to stata file"""
    
#     file = Path(file)
#     # replace all inf to na
#     table.replace([np.inf, -np.inf], np.nan, inplace=True)
    
#     # convert_mixed type to string
#     table = table.convert_dtype_backend("numpy")
#     data_label = table.description
#     variable_labels = table.column_labels.to_dict()
#     table.to_stata(
#         path=file,
#         write_index= (not ignore_index),
#         version=118,
#         data_label=data_label,
#         variable_labels=variable_labels,
#     )
#     if export_metadata:
#         table.describe_columns.to_csv(file.with_suffix(".csv"))
    
# class StataWriter(BaseModel, extra='forbid'):
#     """Stata Writer"""
#     ignore_index: bool = True 
#     export_metadata: bool = False
    
#     def write(self, table: Table, file: str | Path):
        
#         to_stata(table, file, ignore_index=self.ignore_index, export_metadata=self.export_metadata)
        
        
# table_writers = {
#     '.dta': StataWriter()
# }