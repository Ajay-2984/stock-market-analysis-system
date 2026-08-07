import pandas as pd
import sqlite3

connection = sqlite3.connect(
    "stock_market.db"
)

def generate_report():

    query = "SELECT * FROM stocks"

    df = pd.read_sql(
        query,
        connection
    )

    average_price = (
        df['close_price'].mean()
    )

    highest_price = (
        df['high_price'].max()
    )

    lowest_price = (
        df['low_price'].min()
    )

    with open(
        "reports/stock_report.txt",
        "w"
    ) as file:

        file.write(
            "===== STOCK MARKET REPORT =====\n\n"
        )

        file.write(
            f"Average Price: {average_price}\n"
        )

        file.write(
            f"Highest Price: {highest_price}\n"
        )

        file.write(
            f"Lowest Price: {lowest_price}\n"
        )

    print("\nReport Generated")
