import tkinter as tk
from tkinter import messagebox
import sqlite3

# Connect 
conn = sqlite3.connect("Databases/Tkinter_student.db")
cur = conn.cursor()

# Create table
cur.execute('''
    CREATE TABLE IF NOT EXISTS students(
            roll INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL)
''')
conn.commit()

def insert_data(roll, name, department):
    try:
        cur.execute("INSERT INTO Tkinter_students (roll, name, department) VALUES (?,?,?)", (roll, name, department))
        conn.commit()
        messagebox.showinfo("Success", "Student added.")
    
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Roll number already exists")


def fetch_data():
    cur.execute("SELECT * FROM Tkinter_students")
    rows = cur.fetchall()
    return rows


def delete_student(roll):
    cur.execute("DELETE FROM Tkinter_students WHERE roll = ?", (roll,))
    conn.commit()
    messagebox.showinfo("Deleted", f"Roll No. {roll} deleted.")


def search_by_roll(roll):
    cur.execute("SELECT * FROM Tkinter_students WHERE roll = ?", (roll,))
    row = cur.fetchall()
    return row


def clear_entries():
    roll_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    department_entry.delete(0, tk.END)



# GUI SETUP
root = tk.Tk()

root.title("Student DB Manager")

# ENTRY FIELDS
tk.Label(root, text="Roll No.").grid(row=0, column=0)
roll_entry = tk.Entry(root)
roll_entry.grid(row=0, column=1, pady=10)


tk.Label(root, text="Name : ").grid(row=1, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, pady=10)


tk.Label(root, text="Department : ").grid(row=2, column=0)
department_entry = tk.Entry(root)
department_entry.grid(row=2, column=1, pady=10)


# Lsitbox to show data
listbox = tk.Listbox(root, width=50)
listbox.grid(row=6, column=0, columnspan=4, pady=10)


# BUTTON FUNCTIONS
def add_students():
    roll = roll_entry.get()
    name = name_entry.get()
    dept = department_entry.get()
    if roll and name and dept:
        insert_data(int(roll), name, dept)
        viewall()
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Fill all fields")



def viewall():
    listbox.delete(0, tk.END)
    rows = fetch_data()
    for row in rows:
        listbox.insert(tk.END, row)


def delete():
    roll = roll_entry.get()
    if roll:
        delete_student(int(roll))
        viewall()
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "Enter roll to delete")


def search():
    roll = roll_entry.get()
    if roll:
        listbox.delete(0, tk.END)
        result = search_by_roll(int(roll))

        if result:
            listbox.insert(tk.END, result)
        else:
            messagebox.showwarning("Not Found", "No student found")
    else:
        messagebox.showwarning("Input Error", "Enter roll to search")


# BUTTONS
tk.Button(root, text='ADD', command=add_students).grid(row=3, column=0, columnspan=2, pady=5)
tk.Button(root, text='View', command=viewall).grid(row=3, column=1, columnspan=2)
tk.Button(root, text='Delete', command=delete).grid(row=4, column=0, columnspan=2)
tk.Button(root, text='Search', command=search).grid(row=4, column=1, columnspan=2)


root.mainloop()
conn.close()