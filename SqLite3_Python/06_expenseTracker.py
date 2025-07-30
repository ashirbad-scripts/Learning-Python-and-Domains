import sqlite3
import datetime

conn = sqlite3.connect('Databases/expenses.db')
cursor = conn.cursor()

# create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               amount REAL NOT NULL,
               category TEXT NOT NULL,
               date TEXT NOT NULL)
''')
conn.commit()

# Functions
def addExpenses():
    try:
        amount = float(input("Enter amount :- "))
        category = input("Enter Category :- ").lower()
        date = input("Enter date (YY-MM-DD) :- ")

        if date.strip() == "":
            date = datetime.date.today().strftime("%Y-%m-%d")
        
        cursor.execute("INSERT INTO expenses(amount, category, date) VALUES (?,?,?)", (amount, category, date))
        conn.commit()

    except ValueError as e:
        print(e)


def viewSummary():
    print("\nTotal Expenses by category: ")
    cursor.execute("""
        SELECT category, SUM(amount)
                   FROM expenses
                   GROUP BY category
    """)
    rows = cursor.fetchall()
    for eachRow in rows:
        print(f"{eachRow[0].capitalize():<15} => Rs. {eachRow[1]:.2f}") 
    print()


def filterByDate():
    print("\n📅 Filter Expenses by Date Range:")
    start = input("Enter start date (YYYY-MM-DD): ")
    end = input("Enter end date (YYYY-MM-DD): ")
    cursor.execute('''
        SELECT amount, category, date
                   FROM expenses
                   WHERE date BETWEEN ? AND ?
                   ORDER BY date
    ''', (start,end))
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f"Rs.{row[0]:.2f} - {row[1].capitalize()} on {row[2]}")
    else:
        print("NO expenses in this range")
    print()

def main():
    while True:
                print("""
======= 💸 Expense Tracker =======
1. Add Expense
2. View Summary by Category
3. View Expenses by Date Range
4. Exit
""")
                            
                choice = input("Enter Choice : ")
                
                if choice == '1':
                     addExpenses()

                elif choice == '2':
                     viewSummary()

                elif choice == '3':
                     filterByDate()

                elif choice == '4':
                     print("------- Closed -------")
                     conn.close()
                     break
                else:
                     print("Try Again")

if __name__ == "__main__":
     main()

