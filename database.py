import sqlite3

# Database Connection
connection = sqlite3.connect("stock_market.db")

cursor = connection.cursor()


def create_table():

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS stocks (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        company_name TEXT,

        stock_date TEXT,

        open_price REAL,

        high_price REAL,

        low_price REAL,

        close_price REAL,

        volume INTEGER

    )

    """)

    connection.commit()


def is_data_loaded():

    cursor.execute("SELECT COUNT(*) FROM stocks")

    count = cursor.fetchone()[0]

    return count > 0


def clear_table():

    cursor.execute("DELETE FROM stocks")

    connection.commit()

    print("\nOld dataset deleted successfully.")


def insert_data(data):

    for index, row in data.iterrows():

        cursor.execute("""

        INSERT INTO stocks(

            company_name,
            stock_date,
            open_price,
            high_price,
            low_price,
            close_price,
            volume

        )

        VALUES (?, ?, ?, ?, ?, ?, ?)

        """, (

            row["company_name"],
            str(row["date"]),
            row["open_price"],
            row["high_price"],
            row["low_price"],
            row["close_price"],
            row["volume"]

        ))

    connection.commit()

    print("\nDataset Loaded Successfully.")

def total_records():

    cursor.execute("SELECT COUNT(*) FROM stocks")

    return cursor.fetchone()[0]
