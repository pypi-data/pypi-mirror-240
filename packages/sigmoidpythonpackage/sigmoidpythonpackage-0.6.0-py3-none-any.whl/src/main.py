from src.logic import load_file_to_dataframe, display_head, display_tail, display_type, make_changes

if __name__ == "__main__":
    # Load a CSV file
    csv_df = load_file_to_dataframe("my_data.csv", file_format="csv")
    print("Loaded CSV file:")
    print(csv_df)

    # Display head
    print("\nDisplaying top 2 rows:")
    print(display_head(csv_df, n=2))

    # Display tail
    print("\nDisplaying bottom 2 rows:")
    print(display_tail(csv_df, n=2))

    # Display type
    print("\nDisplaying type of DataFrame:")
    print(display_type(csv_df))

    # Make changes
    print("\nMaking changes to DataFrame:")
    modified_df = make_changes(csv_df, column="Age", value=99, index=0)
    print(modified_df)
