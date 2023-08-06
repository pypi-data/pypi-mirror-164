from glob import glob

import pandas as pd


def collect_dfs(pattern, query, **kwargs) -> list:
    return [handle_data_file(f, skiprows=find_row(f, query), **kwargs) for f in find_similar(pattern)]


def convert_minutes_to_hours(data: pd.DataFrame) -> pd.DataFrame:
    for c in data.columns:
        if "minutes" in c.lower():
            data[f"{c.lower().split('minutes')[0]}Hours"] = data[c] / 60.0
    return data


def create_name_column(data: pd.DataFrame) -> pd.DataFrame:
    data["name"] = data["firstName"] + " " + data["lastName"]
    return data


def create_path(base, *args) -> str: return "{}/{}".format(base, "/".join(args))


def find_row(path: str, query: str) -> int:
    try:
        print("Searching lines...")
        return search_file(path, query)[-1] + 1
    except (pd.errors.ParserError, UnicodeDecodeError):
        print("Searching dataframe...")
        return search_excel(path, query)[0] + 2


def find_similar(pattern: str, **kwargs) -> list: return glob(pattern, **kwargs)


def handle_data_file(path, **kwargs) -> pd.DataFrame:
    if "csv" in path:
        return pd.read_csv(path, **kwargs)
    elif "json" in path:
        return pd.read_json(path, **kwargs)
    elif "xls" or "xlsx" in path:
        return pd.read_excel(path, **kwargs)
    else:
        print("Failed to find an operational match for the provided input...")
        raise IOError


def index_of(query: str, *args): return [i for i, j in enumerate(args) if query in j]


def identify_table_matches(path: str, query: str) -> list:
    df = handle_data_file(path)
    return df.index[df[df.columns.to_list()[0]] == query].to_list()


def save_df_as(df, save_as: str):
    if "csv" in save_as:
        df.to_csv(save_as, index=False)
    elif "xls" or "xlsx" in save_as:
        df.to_excel(save_as, index=False)
    else:
        print("IOError: Failed to match save path to a defined operation...")
        raise IOError


def search_file(path: iter, query: str) -> list:
    return [i for i, j in enumerate(open(path, "r")) if query in j or query == j]


def search_excel(path: str, query: str) -> list:
    df = handle_data_file(path)
    return df.index[df[df.columns.to_list()[0]] == query].to_list()
