from typing import List

import numpy as np
import pandas as pd

from tads.utils import collect_dfs, save_df_as


class DocumentProcessor(object):
    data: dict

    def __init__(self, pattern, query, usecols, actions=None, groups=None):
        self.actions: dict = actions
        self.groups: List[str] = groups
        self.pattern: str = pattern
        self.query: str = query
        self.usecols: List[str] = usecols

    def __call__(self, *args, **kwargs):
        self.data = self.clean()

        return self.data[:].to_dict()

    def aggregate(self, **kwargs) -> list:
        return collect_dfs(self.pattern, self.query, **kwargs)

    def combine(self, ignore_index: bool = True, **kwargs) -> dict:
        return pd.concat(self.aggregate(), ignore_index=ignore_index, **kwargs).to_dict()

    def clean(self) -> dict:
        df = pd.DataFrame(self.combine())
        df = df.drop([i for i in df.columns if i not in self.usecols], axis=1)
        df.replace('', np.nan, inplace=True)
        if self.groups:
            df = df.groupby(self.groups, as_index=False)
        if self.actions:
            df = df.agg(self.actions)
        return df.to_dict()

    def export(self, save_as: str):
        save_df_as(pd.DataFrame(self.data), save_as)

    def __repr__(self):
        return f""""{self.clean()}"""
