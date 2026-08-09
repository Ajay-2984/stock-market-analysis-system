import sqlite3
import pandas as pd
import numpy as np

from scripts.ui import title, error, pause

# DATABASE CONNECTION
conn = sqlite3.connect("stock_market.db")


def analyze_data():

    query = "SELECT * FROM stocks LIMIT 10"
    df = pd.read_sql(query, conn)

    # CHECK EMPTY DATA
    if df.empty:
        error("No Data Found")
        return

    title("DATA ANALYSIS")

    average_prices = df.groupby(
        'company_name'
    )['close_price'].mean()

    title("AVERAGE CLOSING PRICE")
    print(average_prices.round(2))

    highest = df.loc[
        df['high_price'].idxmax()
    ]

    title("HIGHEST STOCK PRICE")

    print(f"Company       : {highest['company_name']}")
    print(f"Highest Price : {highest['high_price']:.2f}")

    lowest = df.loc[
        df['low_price'].idxmin()
    ]

    title("LOWEST STOCK PRICE")

    print(f"Company      : {lowest['company_name']}")
    print(f"Lowest Price : {lowest['low_price']:.2f}")

    title("STATISTICAL ANALYSIS")

    print("\nStandard Deviation:")
    print(df['close_price'].std())

    print("\nVariance:")
    print(df['close_price'].var())

    # PROFIT / LOSS
    df['profit_loss'] = (
        df['close_price'] - df['open_price']
    )

    # DAILY RETURN USING NUMPY
    df['daily_return'] = np.log(
        df['close_price'] / df['open_price']
    )

    summary = df.groupby(
        'company_name'
    ).agg({
        'profit_loss': 'mean',
        'daily_return': 'mean'
    })

    title("COMPANY PERFORMANCE SUMMARY")
    print(summary)

    pause()


def search_by_date():

    title("SEARCH BY DATE")

    date = input("Enter Date (YYYY-MM-DD): ")

    query = """
    SELECT *
    FROM stocks
    WHERE stock_date = ?
    """

    df = pd.read_sql(
        query,
        conn,
        params=(date,)
    )

    if df.empty:
        error("No Data Found")
        return

    print(df)

    highest = df.loc[
        df['high_price'].idxmax()
    ]

    title("DAILY HIGHEST PRICE")

    print(f"Company       : {highest['company_name']}")
    print(f"Highest Price : {highest['high_price']:.2f}")

    lowest = df.loc[
        df['low_price'].idxmin()
    ]

    title("DAILY LOWEST PRICE")

    print(f"Company      : {lowest['company_name']}")
    print(f"Lowest Price : {lowest['low_price']:.2f}")

    pause()


def monthly_volume():

    title("MONTHLY VOLUME REPORT")

    month = input("Enter Month (MM): ")
    year = input("Enter Year (YYYY): ")

    query = """
    SELECT
        company_name,
        SUM(volume) AS total_volume
    FROM stocks
    WHERE strftime('%m', stock_date) = ?
    AND strftime('%Y', stock_date) = ?
    GROUP BY company_name
    """

    df = pd.read_sql(
        query,
        conn,
        params=(month, year)
    )

    if df.empty:
        error("No Data Found")
        return

    print(df)

    pause()


def monthly_average_price():

    title("MONTHLY AVERAGE PRICE")

    month = input("Enter Month (MM): ")
    year = input("Enter Year (YYYY): ")

    query = """
    SELECT
        company_name,
        AVG(close_price) AS average_price
    FROM stocks
    WHERE strftime('%m', stock_date) = ?
    AND strftime('%Y', stock_date) = ?
    GROUP BY company_name
    """

    df = pd.read_sql(
        query,
        conn,
        params=(month, year)
    )

    if df.empty:
        error("No Data Found")
        return

    print(df)

    pause()


def stock_price_range():

    title("STOCK PRICE RANGE")

    min_price = float(
        input("Enter Minimum Price: ")
    )

    max_price = float(
        input("Enter Maximum Price: ")
    )

    query = """
    SELECT
        company_name,
        stock_date,
        close_price
    FROM stocks
    WHERE close_price
    BETWEEN ? AND ?
    """

    df = pd.read_sql(
        query,
        conn,
        params=(min_price, max_price)
    )

    if df.empty:
        error("No Stocks Found In This Price Range")
        return

    print(df)

    pause()
