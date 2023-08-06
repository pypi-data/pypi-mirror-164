import pandas as pd
from functools import lru_cache
from datetime import datetime

pandas_excel_parse_args = ["sheet_name", "skiprows", "index_col", "header", "usecols"]


@lru_cache()
def read_excel_file(fname):
    ex = pd.ExcelFile(fname)
    return ex


def find_table_end_horizontal(
    ex, sheet_name: str, index_col: int, lookup_str: str
) -> int:
    """
    Given excel file object, sheet name and index_col, find the end of the table
    by looking for a specific word on the column index specified
    """

    shraw = ex.parse(sheet_name)
    firstfind = -2
    # look in first column for word Source:
    for entry in shraw[shraw.columns[index_col]].str.startswith(lookup_str):
        firstfind += 1
        if entry == True:
            break

    return firstfind


def read_table(fname, **kwargs):
    ex = read_excel_file(fname)
    pandas_args = {x: kwargs[x] for x in kwargs if x in pandas_excel_parse_args}
    sh = ex.parse(**pandas_args)

    if "table_end" in kwargs:
        table_end = find_table_end_horizontal(
            ex,
            kwargs.get("sheet_name"),
            index_col=kwargs["table_end"]["index_col"],
            lookup_str=kwargs["table_end"]["lookup_str"],
        )
        sh = sh.head(table_end)

    if "horizontal_table" in kwargs and kwargs["horizontal_table"]:
        sh = sh.T

    if "select_dates_for_index_col" in kwargs and kwargs["select_dates_for_index_col"]:
        sh = sh[sh.apply(lambda x: type(x.name) == datetime, 1)]
        sh.index = pd.to_datetime(sh.index)

    return sh


def read_long_format_table(fname, **kwargs):
    sh = read_table(fname, **kwargs)

    dimension_cols = kwargs.get("dimension_cols")
    value_col = kwargs.get("value_col")
    sh["index"] = sh.apply(
        lambda x: ".".join(["%s" for x in dimension_cols])
        % tuple([x[y] for y in dimension_cols]),
        1,
    )
    sh["date_as_index"] = sh.index
    sh = sh.groupby(["date_as_index", "index"]).mean().unstack()[value_col]
    return sh
