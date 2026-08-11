import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


def create_visualizations():

    # Connect to Database
    with sqlite3.connect("stock_market.db") as connection:

        query = "SELECT * FROM stocks"

        df = pd.read_sql(query, connection)

    # -----------------------------
    # Check if data exists
    # -----------------------------
    if df.empty:
        print("\nNo data found in database.")
        print("Please load the dataset first.")
        return

    # -----------------------------
    # Convert Date Column
    # -----------------------------
    df["stock_date"] = pd.to_datetime(
        df["stock_date"],
        errors="coerce"
    )

    # Remove invalid dates
    df = df.dropna(subset=["stock_date"])

    # Sort Data
    df = df.sort_values("stock_date")

    # -----------------------------
    # Create Charts Folder
    # -----------------------------
    os.makedirs("charts", exist_ok=True)

    print("\nGenerating Charts...")

    # ======================================
    # 1. Closing Price Trend
    # ======================================

    plt.figure(figsize=(12,6))

    for company in df["company_name"].unique():

        company_df = df[df["company_name"] == company]

        company_df = company_df.sort_values("stock_date")

        plt.plot(
            company_df["stock_date"],
            company_df["close_price"],
            marker="o",
            linewidth=2,
            label=company
        )

    plt.title("Closing Price Trend")

    plt.xlabel("Date")

    plt.ylabel("Closing Price")

    plt.legend()

    plt.grid(True)

    plt.tight_layout()

    plt.savefig("charts/closing_price_trend.png")

    plt.close()

    # ======================================
    # 2. Average Closing Price
    # ======================================

    avg = df.groupby("company_name")["close_price"].mean()

    plt.figure(figsize=(8,5))

    avg.plot(kind="bar")

    plt.title("Average Closing Price")

    plt.xlabel("Company")

    plt.ylabel("Average Closing Price")

    plt.tight_layout()

    plt.savefig("charts/company_average_price.png")

    plt.close()

    # ======================================
    # 3. Volume Distribution
    # ======================================

    volume = df.groupby("company_name")["volume"].sum()

    plt.figure(figsize=(7,7))

    plt.pie(
        volume,
        labels=volume.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Volume Distribution")

    plt.tight_layout()

    plt.savefig("charts/volume_distribution.png")

    plt.close()

    # ======================================
    # 4. Histogram
    # ======================================

    plt.figure(figsize=(8,5))

    plt.hist(
        df["close_price"],
        bins=20,
        edgecolor="black"
    )

    plt.title("Closing Price Distribution")

    plt.xlabel("Closing Price")

    plt.ylabel("Frequency")

    plt.tight_layout()

    plt.savefig("charts/price_histogram.png")

    plt.close()

    # ======================================
    # 5. Scatter Plot
    # ======================================

    plt.figure(figsize=(8,5))

    plt.scatter(
        df["open_price"],
        df["close_price"]
    )

    plt.title("Open Price vs Close Price")

    plt.xlabel("Open Price")

    plt.ylabel("Close Price")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig("charts/open_vs_close_scatter.png")

    plt.close()

    print("\nCharts saved inside 'charts' folder.")

    print("\nGenerated Charts:")

    print("1. Closing Price Trend")

    print("2. Company Average Closing Price")

    print("3. Volume Distribution")

    print("4. Closing Price Histogram")

    print("5. Open vs Close Scatter Plot")
