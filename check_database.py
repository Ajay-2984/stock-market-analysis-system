import sqlite3
import pandas as pd

connection = sqlite3.connect("stock_market.db")

df = pd.read_sql(
    "SELECT company_name, stock_date FROM stocks",
    connection
)

print(df.head(30))
