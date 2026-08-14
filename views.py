import os


# ------------------------------------------
# Clear Screen
# ------------------------------------------

def clear_screen():

    os.system("cls" if os.name == "nt" else "clear")


# ------------------------------------------
# Main Menu
# ------------------------------------------

def display_menu():

    clear_screen()

    print("=" * 60)

    print("        STOCK MARKET ANALYTICS SYSTEM")

    print("=" * 60)

    print("Version   : 2.0")

    print("Developer : Ajay K")

    print("=" * 60)

    print()

    print("1. Dataset Management")

    print("2. Record Management")

    print("3. Stock Analysis")

    print("4. Trend Analysis")

    print("5. Company Comparison")

    print("6. Statistical Analysis")

    print("7. Data Visualization")

    print("8. Seaborn Analytics")

    print("9. Reports")

    print("10. Search & Filter")

    print("11. Export")

    print("12. Exit")

    print()

    print("=" * 60)


# ------------------------------------------
# Record Menu
# ------------------------------------------

def record_menu():

    print("\n" + "=" * 50)

    print("          RECORD MANAGEMENT")

    print("=" * 50)

    print("1. Insert Record")

    print("2. View Records")

    print("3. Delete Record")

    print("4. Back")

    print("=" * 50)


# ------------------------------------------
# Analysis Menu
# ------------------------------------------

def analysis_menu():

    print("\n" + "=" * 50)

    print("            STOCK ANALYSIS")

    print("=" * 50)

    print("1. Overall Analysis")

    print("2. Search by Date")

    print("3. Monthly Volume")

    print("4. Monthly Average Price")

    print("5. Stock Price Range")

    print("6. Back")

    print("=" * 50)
def search_menu():

    print("\n" + "=" * 50)
    print("         SEARCH & FILTER")
    print("=" * 50)
    print("1. Search by Company")
    print("2. Back")
    print("=" * 50)
