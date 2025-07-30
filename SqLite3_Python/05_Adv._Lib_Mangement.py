import sqlite3
import datetime

# Connect to SQLite DB
conn = sqlite3.connect("Databases/library.db")
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS books(
               book_id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT NOT NULL,
               author TEXT NOT NULL,
               available INTEGER DEFAULT 1)
""")

# Borrowers
cursor.execute("""
    CREATE TABLE IF NOT EXISTS borrowers(
               borrower_id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT NOT NULL,
               email TEXT NOT NULL,
            )
""")


# Borrowed
cursor.execute("""
    CREATE TABLE IF NOT EXISTS borrowed(
               borrow_id INTEGER PRIMARY KEY AUTOINCREMENT,
               book_id INTEGER,
               borrower_id INTEGER,
               borrow_date TEXT,
               FOREIGN KEY(book_id) REFERENCES books(book_id),
               FOREIGN KEY(borrower_id) REFERENCES borrowers(borrow_id)
            )
""")
conn.commit()

# FUNCTIONs
def addBook():
    title = input("Enter book title :- ")
    author = input("Enter author :- ")
    cursor.execute("INSERT INTO books(title, author) VALUES (?,?)", (title, author))
    conn.commit()
    print("Book added Successfully")

def addBorrower():
    name = input("Enter Name :- ")
    email = input("Enter Email :- ")
    cursor.execute("INSERT INTO borrowers (name, email) VALUES (?,?)", (name, email))
    conn.commit()
    print("Borrower added sucessfully\n")

def borrowBooks():
    book_id = int(input("Enter Book ID to borrow: "))
    borrower_id = int(input("Enter Borrower ID: "))

    # Check if book is available
    cursor.execute("SELECT available FROM books WHERE book_id = ?", (book_id,))
    result = cursor.fetchone()
    if result and result[0] == 1:
        borrow_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO borrowed (book_id, borrower_id, borrow_date) VALUES (?, ?, ?)",
                       (book_id, borrower_id, borrow_date))
        cursor.execute("UPDATE books SET available = 0 WHERE book_id = ?", (book_id,))
        conn.commit()
        print("Book borrowed successfully")
    else:
        print("Not available")

def returnBooks(book_id):
    return
    

# .........Lacks motivation...........................................