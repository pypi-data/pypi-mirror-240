import pandas as pd
from src.logic import load_file_to_dataframe

def test_load_csv():
    csv_content = "Name,Age\nJohn,25\nJane,30\n"
    csv_path = "src/test.csv"

    # Write the test CSV file
    with open(csv_path, "w", encoding="utf-8") as csv_file:
        csv_file.write(csv_content)

    # Load CSV and check the DataFrame
    df = load_file_to_dataframe(csv_path, file_format="csv")
    expected_df = pd.DataFrame({"Name": ["John", "Jane"], "Age": [25, 30]})
    pd.testing.assert_frame_equal(df, expected_df)

def test_load_excel():
    excel_content = {"Sheet1": {"Name": ["Alice", "Bob"], "Age": [22, 28]}}

    # Write the test Excel file
    excel_path = "src/test.xlsx"
    with pd.ExcelWriter(excel_path, engine="xlsxwriter") as writer:
        for sheet_name, content in excel_content.items():
            pd.DataFrame(content).to_excel(writer, sheet_name=sheet_name, index=False)

    # Load Excel and check the DataFrame
    df = load_file_to_dataframe(excel_path, file_format="excel")
    expected_df = pd.DataFrame(excel_content["Sheet1"])
    pd.testing.assert_frame_equal(df, expected_df)
