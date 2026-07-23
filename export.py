import os
import sqlite3
import pandas as pd

from scripts.ui import title, success, error, pause
from scripts.logger import log_info, log_error


def export_menu():

    title("EXPORT DATA")

    print("1. Export to Excel")
    print("2. Export to CSV")
    print("3. Export to Text File")
    print("4. Back")

    print("=" * 65)


def export_data():

    try:

        os.makedirs("exports", exist_ok=True)

        connection = sqlite3.connect("stock_market.db")

        query = "SELECT * FROM stocks"

        df = pd.read_sql(query, connection)

        connection.close()

        if df.empty:

            error("No Data Available To Export")

            log_error("Export Failed : No Data")

            pause()

            return

        while True:

            export_menu()

            choice = input("\nEnter your choice : ")

            # ----------------------------------
            # Excel
            # ----------------------------------

            if choice == "1":

                file_path = "exports/Stock_Data.xlsx"

                df.to_excel(
                    file_path,
                    index=False
                )

                success("Excel File Exported Successfully")

                print(f"Saved To : {file_path}")

                log_info("Excel File Exported")

                pause()

            # ----------------------------------
            # CSV
            # ----------------------------------

            elif choice == "2":

                file_path = "exports/Stock_Data.csv"

                df.to_csv(
                    file_path,
                    index=False
                )

                success("CSV File Exported Successfully")

                print(f"Saved To : {file_path}")

                log_info("CSV File Exported")

                pause()

            # ----------------------------------
            # Text
            # ----------------------------------

            elif choice == "3":

                file_path = "exports/Stock_Data.txt"

                with open(file_path, "w") as file:

                    file.write(df.to_string(index=False))

                success("Text File Exported Successfully")

                print(f"Saved To : {file_path}")

                log_info("Text File Exported")

                pause()

            elif choice == "4":

                break

            else:

                error("Invalid Choice")

                pause()

    except Exception as e:

        error("Export Failed")

        log_error(f"Export Error : {e}")
