import os.path
from glob import glob
from typing import List

import numpy as np
import pandas as pd


class Tipsheet(object):
    columns: List[str]
    data: pd.DataFrame
    folder: str
    files: List[str] = []
    group_actions: dict
    groups: List[str]
    pattern: str = "ServerTipDeclarations_*"
    save_as: str = None
    skip_at: str = "ServerTipDeclarationDataSet_GenerateTipDeclaration"
    usecols: List[str] = ["firstName", "lastName", "chargeTips", "cashTips"]

    def __init__(self, folder: str = os.path.curdir, save_as: str = None):
        self.folder = folder
        self.save_as = save_as

        if folder:
            self.pattern = "{}/{}".format(folder, self.pattern)

        self.files = glob(self.pattern)
        self.data = pd.concat(self.aggregate(), ignore_index=True)
        self.columns = self.data.columns.to_list()

        if self.save_as:
            self.export()

    @staticmethod
    def handler(filepath, **kwargs):
        if "csv" in filepath:
            return pd.read_csv(filepath, **kwargs)
        elif "xls" or "xlsx" in filepath:
            return pd.read_excel(filepath, **kwargs)
        else:
            print("IOError: Failed to match the input to a defined operation")
            raise IOError

    def aggregate(self) -> List[pd.DataFrame]: return [self.handler(f, skiprows=self.detect(f)) for f in self.files]

    def clean(self):
        df = self.data[:]
        df = df.drop([i for i in self.columns if i not in self.usecols], axis=1)
        df.replace('', np.nan, inplace=True)
        df = df.dropna()
        for col in df.columns:
            if "name" in col.lower():
                df[col] = df[col].str.lower()
        df["name"] = df.firstName + " " + df.lastName
        return df

    def detect(self, filepath: str):
        if "csv" in filepath:
            return [i for i, j in enumerate(open(filepath, "r")) if self.skip_at in j]
        elif "xls" or "xlsx" in filepath:
            tmp = self.handler(filepath)
            return tmp.index[tmp[tmp.columns.to_list()[0]] == self.skip_at].to_list()[0] + 2

    def export(self):
        if "csv" in self.save_as:
            self.data.to_csv(self.save_as, index=False)
        elif "xls" or "xlsx" in self.save_as:
            self.data.to_excel(self.save_as, index=False)
        else:
            print("IOError: Failed to match save path to a defined operation...")
            raise IOError

    def __repr__(self):
        return f""""{self.clean()}"""
