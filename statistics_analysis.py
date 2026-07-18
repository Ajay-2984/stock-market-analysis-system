import sqlite3
import pandas as pd
import numpy as np

# Connect to SQLite Database
connection = sqlite3.connect("stock_market.db")


def statistical_analysis():

    # Read data from database
    query = "SELECT * FROM stocks"

    df = pd.read_sql(query, connection)

    print("\n==========================================")
    print("      STOCK STATISTICAL ANALYSIS")
    print("==========================================")

    # Closing Price Column
    prices = df["close_price"]

    # Mean
    mean = prices.mean()

    # Median
    median = prices.median()

    # Mode
    mode = prices.mode()

    # Maximum
    maximum = prices.max()

    # Minimum
    minimum = prices.min()

    # Range
    price_range = maximum - minimum

    # Standard Deviation
    std = np.std(prices)

    # Variance
    variance = np.var(prices)

    # Quartiles
    q1 = prices.quantile(0.25)

    q2 = prices.quantile(0.50)

    q3 = prices.quantile(0.75)

    # Percentiles
    p25 = np.percentile(prices, 25)

    p50 = np.percentile(prices, 50)

    p75 = np.percentile(prices, 75)

    p90 = np.percentile(prices, 90)

    # Coefficient of Variation
    cv = (std / mean) * 100

    # Display Results

    print(f"\nMean                 : {mean:.2f}")

    print(f"Median               : {median:.2f}")

    print(f"Mode                 : {mode.iloc[0]:.2f}")

    print(f"Maximum Price        : {maximum:.2f}")

    print(f"Minimum Price        : {minimum:.2f}")

    print(f"Price Range          : {price_range:.2f}")

    print(f"Standard Deviation   : {std:.2f}")

    print(f"Variance             : {variance:.2f}")

    print("\n------------- Quartiles -------------")

    print(f"Q1 (25%)             : {q1:.2f}")

    print(f"Q2 (50%)             : {q2:.2f}")

    print(f"Q3 (75%)             : {q3:.2f}")

    print("\n------------ Percentiles ------------")

    print(f"25th Percentile      : {p25:.2f}")

    print(f"50th Percentile      : {p50:.2f}")

    print(f"75th Percentile      : {p75:.2f}")

    print(f"90th Percentile      : {p90:.2f}")

    print(f"\nCoefficient of Variation : {cv:.2f}%")

    print("\n==========================================")
