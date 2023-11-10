import pandas as pd

def load_file_to_dataframe(file_path, file_format):

    if file_format == "csv":
        df = pd.read_csv(file_path)
    elif file_format == "excel":
        df = pd.read_excel(file_path)

    return df

def display_head(df, n=5):
  
    return df.head(n)

def display_tail(df, n=5):

    return df.tail(n)

def display_type(df):

    return type(df)

def make_changes(df, column, value, index=None):

    if index is not None:
        df.at[index, column] = value
    else:
        df[column] = value

    return df