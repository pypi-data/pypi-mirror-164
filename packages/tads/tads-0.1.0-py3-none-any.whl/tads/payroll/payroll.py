import os
from typing import List

import numpy as np
import pandas as pd

from app.core.primitives import PAYROLL_COLUMNS
from .timesheet import TimesheetActor
from .tipsheet import TipsheetActor


class Payroll(object):
    columns: List[str]
    data: pd.DataFrame
    filepath: str
    save_as: str = None
    skiprows: int = 0
    usecols: list = PAYROLL_COLUMNS

    def __init__(self, filepath: str, save_as: str = None):
        self.filepath = filepath
        self.save_as = save_as
        self.folder = os.path.dirname(self.filepath)

        self.data = self.handler(self.filepath, skiprows=self.skiprows, usecols=self.usecols)
        self.columns = self.data.columns.to_list()

        self.data = self.timesheet()
        self.data = self.tipsheet()

        self.data.replace(np.nan, 0.0, inplace=True)

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

    def timesheet(self):
        df = self.data[:]
        time = TimesheetActor(self.folder).clean()
        for i, j, k in zip(time.name, time.minorJob, range(time.shape[0])):
            df.loc[(df.Name.str.lower() == i) & (df["Default Job"] == j), "E Regular Hours"] = time.regularHours[k]
            df.loc[(df.Name.str.lower() == i) & (df["Default Job"] == j), "E Overtime Hours"] = time.overtimeHours[k]
        return df

    def tipsheet(self):
        df = self.data[:]
        tips = TipsheetActor(os.path.dirname(self.filepath)).clean()
        for i, j in enumerate(tips.name):
            try:
                df.loc[df.Name.str.lower() == j, "E Charge Tips Amount"] = tips.chargeTips[i]
            except KeyError:
                print("Key Error: Skipping row {} of {}".format(i, tips.shape[0]))
        self.data = df
        return self.data

    def export(self):
        if "csv" in self.save_as:
            self.data.to_csv(self.save_as, index=False)
        elif "xls" or "xlsx" in self.save_as:
            self.data.to_excel(self.save_as, index=False)
        else:
            print("IOError: Failed to match save path to a defined operation...")
            raise IOError

    def __repr__(self):
        return f""""{self.data}"""
