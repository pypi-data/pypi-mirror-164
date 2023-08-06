import glob
import os
from typing import List

import pandas as pd


class TimesheetActor(object):
    group_actions: dict = {i: "sum" for i in ["regularMinutes", "overtimeMinutes", "minutesWorked"]}
    columns: List[str]
    data: pd.DataFrame
    files: List[str]
    folder: str
    groups: list = ["minorJob", "name"]
    pattern: str = "EmployeeTimesheet_*.csv"
    save_as: str = None
    skip_at: str = "CostAnalysisDataset_GenerateCostAnalysisReport_LabourCosts"
    usecols: str = [
        "name",
        "minorJob",
        "minutesWorked",
        "startDate",
        "endDate",
        "regularMinutes",
        "overtimeMinutes"
    ]

    def __init__(self, folder: str = os.path.curdir, save_as: str = None):
        self.folder = folder

        self.files = glob.glob("/".join([self.folder, self.pattern]))

        self.data = pd.concat(self.aggregate(), ignore_index=True)
        self.data = self.clean()

        if self.save_as:
            self.export()

    @staticmethod
    def convert_minutes_to_hours(data: pd.DataFrame) -> pd.DataFrame:
        for c in data.columns:
            if "minutes" in c.lower():
                data[f"{c.lower().split('minutes')[0]}Hours"] = data[c] / 60.0
        return data

    @staticmethod
    def handler(filepath, **kwargs) -> pd.DataFrame:
        if "csv" in filepath:
            return pd.read_csv(filepath, **kwargs)
        elif "xls" or "xlsx" in filepath:
            return pd.read_excel(filepath, **kwargs)
        else:
            print("IOError: Failed to match the input to a defined operation")
            raise IOError

    def aggregate(self) -> List[pd.DataFrame]:
        return [self.handler(f, skiprows=int(self.detect(f)[0] + 1)) for f in self.files]

    def clean(self):
        df = self.data[:]
        df = df.groupby(self.groups, as_index=False).agg(self.group_actions)
        df = self.convert_minutes_to_hours(df)
        for col in df.columns:
            if "name" in col.lower():
                df[col] = df[col].str.lower()
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


if __name__ == "__main__":
    test_data_dir: str = "D:\\OneDrive - Scattered-Systems, LLC\\clients\\TaD's Louisiana Cooking\\payroll\\08-07-2022"
    test_ts = TimesheetActor(test_data_dir)
    print(test_ts.data)
