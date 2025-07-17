import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import pandas as pd
import pytest


def load_test_data(sheet_name="apis", action=None, parametrize=False):
    df = pd.read_excel("test_data/test_cases_BOOKS.xlsx", sheet_name=sheet_name)
    df["action"] = df["action"].astype(str).str.strip().str.lower()

    if action:
        action = action.strip().lower()
        df = df[df["action"] == action]

    df = df.fillna("").infer_objects(copy=False)
    records = df.to_dict("records")
    ids = df["note"].fillna("no_note").tolist()

    if parametrize:
        return "data", [pytest.param(row, id=ids[i]) for i, row in enumerate(records)]

    return records, ids
