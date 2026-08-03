import pandas as pd


def load_data():

    # Read all sheets from Excel
    all_sheets = pd.read_excel(
        "data/stock_market_dataset.xlsx",
        sheet_name=None
    )

    print("\n========== SHEETS FOUND ==========")
    print(list(all_sheets.keys()))

    dataframes = []

    # Process each sheet
    for sheet_name, df in all_sheets.items():

        print(f"\nLoading Sheet : {sheet_name}")

        # Remove empty rows
        df = df.dropna(how="all")

        # Rename columns
        df.columns = [
            "company_name",
            "date",
            "open_price",
            "high_price",
            "low_price",
            "close_price",
            "volume"
        ]

        dataframes.append(df)

    # Combine all sheets
    final_df = pd.concat(
        dataframes,
        ignore_index=True
    )

    print("\n========== DATA LOADED ==========")

    print(final_df.head())

    print("\nColumns:")

    print(final_df.columns)

    print("\nCompanies:")

    print(final_df["company_name"].unique())

    print("\nTotal Records :", len(final_df))

    return final_df
