import numpy as np
import pandas as pd

from .primitives import PAYROLL_USECOLS, TIMESHEET_USECOLS, TIPSHEET_USECOLS
from .process import DocumentProcessor
from .utils import handle_data_file, save_df_as, convert_minutes_to_hours, create_name_column


def timesheet(df):
    doc = DocumentProcessor(
        actions={i: "sum" for i in ["regularMinutes", "overtimeMinutes", "minutesWorked"]},
        groups=["minorJob", "name"],
        pattern=".artifacts/files/EmployeeTimesheet_*",
        query="CostAnalysisDataset_GenerateCostAnalysisReport_LabourCosts",
        usecols=TIMESHEET_USECOLS
    )
    times = convert_minutes_to_hours(pd.DataFrame(doc.clean()))
    for i, j, k in zip(times.name, times.minorJob, range(times.shape[0])):
        df.loc[(df.Name.str.lower() == i) & (df["Default Job"] == j), "E Regular Hours"] = times.regularHours[k]
        df.loc[(df.Name.str.lower() == i) & (df["Default Job"] == j), "E Overtime Hours"] = times.overtimeHours[k]
    return df


def tipsheet(df):
    doc = DocumentProcessor(
        pattern=".artifacts/files/ServerTipDeclarations_*",
        query="ServerTipDeclarationDataSet_GenerateTipDeclaration",
        usecols=TIPSHEET_USECOLS
    )
    tips = create_name_column(pd.DataFrame(doc.clean()))
    print(tips.columns)
    for i, j in enumerate(tips["name"]):
        try:
            df.loc[df.Name.str.lower() == j, "E Charge Tips Amount"] = tips["chargeTips"][i]
        except KeyError:
            print("Key Error: Skipping row {} of {}".format(i, tips.shape[0]))
    return df


class Payroll(object):
    data: dict
    usecols: list = PAYROLL_USECOLS

    def __init__(self, filepath):
        self.path: str = filepath
        self.run()

    def __call__(self, *args, **kwargs):
        df = pd.DataFrame(self.data)
        if kwargs["save_as"]:
            save_df_as(df, kwargs["save_as"])
        return df

    def run(self) -> pd.DataFrame:
        df = handle_data_file(self.path, usecols=self.usecols)
        df = timesheet(df)
        df = tipsheet(df)
        df.replace(np.nan, 0.0, inplace=True)
        self.data = df.to_dict()
        return df


if __name__ == "__main__":
    tp = Payroll(".artifacts/files/Payroll.xls")
