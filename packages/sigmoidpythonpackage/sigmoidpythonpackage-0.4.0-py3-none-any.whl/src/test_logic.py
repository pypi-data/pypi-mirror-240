import pandas as pd
from src.logic import load_file_to_dataframe, display_head, display_tail, display_type, make_changes

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

def test_display_head():
    data = {"Name": ["John", "Jane", "Bob", "Alice"], "Age": [25, 30, 22, 28]}
    df = pd.DataFrame(data)
    expected_result = df.head(2)
    result = display_head(df, n=2)
    pd.testing.assert_frame_equal(result, expected_result)

def test_display_tail():
    data = {"Name": ["John", "Jane", "Bob", "Alice"], "Age": [25, 30, 22, 28]}
    df = pd.DataFrame(data)
    expected_result = df.tail(3)
    result = display_tail(df, n=3)
    pd.testing.assert_frame_equal(result, expected_result)

def test_display_type():
    data = {"Name": ["John", "Jane", "Bob", "Alice"], "Age": [25, 30, 22, 28]}
    df = pd.DataFrame(data)
    expected_result = type(df)
    result = display_type(df)
    assert result == expected_result

def test_make_changes():
    data = {"Name": ["John", "Jane", "Bob", "Alice"], "Age": [25, 30, 22, 28]}
    df = pd.DataFrame(data)
    expected_result = pd.DataFrame({"Name": ["John", "Jane", "Bob", "Alice"], "Age": [99, 30, 22, 28]})
    result = make_changes(df, column="Age", value=99, index=0)
    pd.testing.assert_frame_equal(result, expected_result)