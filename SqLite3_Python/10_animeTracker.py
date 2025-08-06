import sqlite3
import tkinter as tk
from tkinter import messagebox
import csv

conn = sqlite3.connect("Databases/Anime_Tracker.db")
cursor = conn.cursor()

# Create anime table.
cursor.execute('''
    CREATE TABLE IF NOT EXISTS anime(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT NOT NULL UNIQUE,
               genre TEXT,
               status TEXT DEFAULT 'WATCHING',
               rating INTEGER)
''')
conn.commit()


# FUNcTIOS 
def add_anime():
    title = entry_title.get().strip()
    genre = entry_genre.get().strip()
    cursor.execute("INSERT INTO anime(title, genre) VALUES (?,?)", (title, genre))
    conn.commit()
    messagebox.showinfo("Success", f"'{title}' added.")


def mark_Watched():
    title = entry_title.get().strip()
    cursor.execute("UPDATE anime SET status = 'Watched' WHERE title = ?", (title,))

    if cursor.rowcount:
        conn.commit()
        messagebox.showinfo("Updated", "Mark as watched")
    else:
        messagebox.showerror("Not Found", "Check spelling")


def anime_dropped():
    title = entry_title.get().strip()
    cursor.execute("INSERT anime SET status = 'Dropped' WHERE title = ?", (title))
    if cursor.rowcount:
        conn.commit()
        messagebox.showinfo("Updated", f"{title} Mark as dropped")
    else:
        messagebox.showinfo("Not found", f"{title} not found")


def set_rating():
    title = entry_title.get().strip()
    try:
        rating = int(entry_rating.get().strip())
        if not (rating >0 and rating <10):
            raise ValueError
    except ValueError:
        messagebox.showerror("Input Error", "Rating must be an integer")
    
    cursor.execute("UPDATE anime SET rating = ? WHERE title = ?", (rating, title))
    if cursor.rowcount:
        conn.commit()
        messagebox.showinfo("Updated", "Rated")
    else:
        messagebox.showerror("Not Found", f"{title} not found")


def delete_anime():
    try:
        anime_id = int(entry_id.get().strip())
    except ValueError:
        messagebox.showerror("input Error", "ID must be a number")
        return
    
    cursor.execute("DELETE FROM anime WHERE id = ?", (anime_id,))
    if cursor.rowcount !=0:
        conn.commit()
        messagebox.showinfo("Deleted", "Deleted Successfully")
    else:
        messagebox.showerror("Not Found", f"Anime with ID {anime_id} not found")


def export_to_csv():
    cursor.execute("SELECT * FROM anime")
    records = cursor.fetchall()
    if not records:
        messagebox.showinfo("No Data", "Nothing to export")
        return
    with open("Generated_CSV's/anime_status.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Title", "Genre", "Status", "Rating"])
        writer.writerows(records)
    messagebox.showinfo("Exported", "Sucessfully exported")
    

def clear_input():
    entry_id.delete(0, tk.END)
    entry_title.delete(0, tk.END)
    entry_genre.delete(0, tk.END)
    entry_rating.delete(0, tk.END)








# UI SETUP
root = tk.Tk()
root.title("Anime Tracker")

# labels and entry field
tk.Label(root, text="ID").grid(row=0, column=0, padx=5, pady=5)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1, padx=5, pady=5)


tk.Label(root, text="Title").grid(row=1, column=0, padx=5, pady=5)
entry_title = tk.Entry(root)
entry_title.grid(row=1, column=1, padx=5, pady=5)


tk.Label(root, text="Genre").grid(row=2, column=0, padx=5, pady=5)
entry_genre = tk.Entry(root)
entry_genre.grid(row=2, column=1, padx=5, pady=5)


tk.Label(root, text="Rating").grid(row=3, column=0, padx=5, pady=5)
entry_rating = tk.Entry(root)
entry_rating.grid(row=3, column=1, padx=5, pady=5)


# Button Frames
btn_frame = tk.Frame(root)
btn_frame.grid(row=4, column=1, columnspan=2, pady=10)


tk.Button(btn_frame, text="Add anime",command=add_anime).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Mark Watched",command=mark_Watched).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Mark Dropped",command=anime_dropped).grid(row=2, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Set Rating",command=set_rating).grid(row=3, column=0, columnspan=2, padx=5, pady=5)
tk.Button(btn_frame, text="Delete",command=delete_anime).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Export",command=export_to_csv).grid(row=1, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Done",command=clear_input).grid(row=2, column=1, padx=5, pady=5)


# Text widget for output diplay
output = tk.Text(root, height=12, width=70)
output.grid(row=5, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()
conn.close()
