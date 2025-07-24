# Ignore future warnings to keep the test output clean
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

# Import required modules
import pandas as pd
import pytest

# Utility function to load and filter test data from an Excel file for API testing.
# Allows filtering by action and supports pytest parameterization.
def load_test_data(
    sheet_name="apis",
    action=None,
    parametrize=False,
    excel_file="test_data/test_cases_RESOURCE.xlsx"
):
    # Load the specified sheet from the Excel file into a DataFrame
    df = pd.read_excel(excel_file, sheet_name=sheet_name)

    # Normalize the 'action' column: ensure all actions are lowercase and trimmed of whitespace
    df["action"] = df["action"].astype(str).str.strip().str.lower()

    # If an action filter is provided, keep only rows that match the action
    if action:
        action = action.strip().lower()
        df = df[df["action"] == action]

    # Replace NaN values with empty strings and infer correct data types
    df = df.fillna("").infer_objects(copy=False)

    # Convert the DataFrame into a list of dictionaries, one for each test case
    records = df.to_dict("records")

    # Prepare a list of test IDs (from the 'note' column, or "no_note" if not provided)
    ids = df["note"].fillna("no_note").tolist()

    # If pytest parameterization is requested, return a tuple in the format pytest expects
    if parametrize:
        return "data", [pytest.param(row, id=ids[i]) for i, row in enumerate(records)]

    # Otherwise, return the records and IDs as regular lists
    return records, ids
