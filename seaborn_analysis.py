import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def seaborn_analysis():

    # Connect to Database
    connection = sqlite3.connect("stock_market.db")

    query = "SELECT * FROM stocks"

    df = pd.read_sql(query, connection)

    connection.close()

    # Check if data exists
    if df.empty:

        print("\nNo data available.")

        return

    # Convert Date
    df["stock_date"] = pd.to_datetime(
        df["stock_date"],
        errors="coerce"
    )

    # Create charts folder
    os.makedirs("charts", exist_ok=True)

    print("\nGenerating Seaborn Charts...")

    # ==========================================
    # 1. Correlation Heatmap
    # ==========================================

    plt.figure(figsize=(10,6))

    numeric_columns = df[[
        "open_price",
        "high_price",
        "low_price",
        "close_price",
        "volume"
    ]]

    sns.heatmap(
        numeric_columns.corr(),
        annot=True,
        cmap="coolwarm"
    )

    plt.title("Stock Correlation Heatmap")

    plt.tight_layout()

    plt.savefig("charts/heatmap.png")

    plt.close()

    # ==========================================
    # 2. Box Plot
    # ==========================================

    plt.figure(figsize=(10,6))

    sns.boxplot(
        x="company_name",
        y="close_price",
        data=df
    )

    plt.title("Company Closing Price Distribution")

    plt.tight_layout()

    plt.savefig("charts/boxplot.png")

    plt.close()

    # ==========================================
    # 3. Violin Plot
    # ==========================================

    plt.figure(figsize=(10,6))

    sns.violinplot(
        x="company_name",
        y="close_price",
        data=df
    )

    plt.title("Closing Price Density")

    plt.tight_layout()

    plt.savefig("charts/violinplot.png")

    plt.close()

    # ==========================================
    # 4. Pair Plot
    # ==========================================

    pair = sns.pairplot(

        df[[
            "open_price",
            "high_price",
            "low_price",
            "close_price",
            "volume"
        ]]

    )

    pair.fig.suptitle(
        "Pair Plot of Stock Features",
        y=1.02
    )

    pair.savefig("charts/pairplot.png")

    plt.close()

    print("\n====================================")

    print("Seaborn Charts Generated Successfully")

    print("====================================")

    print("\nCharts Saved Inside")

    print("charts/")

    print("\n1. heatmap.png")

    print("2. boxplot.png")

    print("3. violinplot.png")

    print("4. pairplot.png")
