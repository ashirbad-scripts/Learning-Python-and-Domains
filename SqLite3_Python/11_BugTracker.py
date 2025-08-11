import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
import csv

conn = sqlite3.connect("Databases/BugTracker.db")
cursor = conn.cursor()
cursor.execute('PRAGMA foreign_keys = ON')

# create user table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
               user_id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL
               )
''')

# Create projects table
cursor.execute('''
CREATE TABLE IF NOT EXISTS projects(
               project_id INTEGER PRIMARY KEY AUTOINCREMENT,
               project_name TEXT NOT NULL UNIQUE
               )
''')

#create issues tables 
cursor.execute('''
CREATE TABLE IF NOT EXISTS issues(
               issue_id INTEGER PRIMARY KEY AUTOINCREMENT,
               project_id INTEGER NOT NULL,
               user_id INTEGER NOT NULL,
               description TEXT NOT NULL,
               status TEXT DEFAULT 'unsolved',
               FOREIGN KEY (project_id) REFERENCES projects(project_id),
               FOREIGN KEY (user_id) REFERENCES users(user_id)
               )
''')
conn.commit()

# HELPER FUNCTIONS
def refresh_users():
    cursor.execute("SELECT user_id, name FROM users")
    return [f"{uid} : {um}" for uid, um in cursor.fetchall()]

def refresh_projects():
    cursor.execute("SELECT project_id, project_name FROM projects")
    return [f"{pid} : {pn}" for pid, pn in cursor.fetchall()]

def get_issue_ids():
    cursor.execute("SELECT issue_id FROM issues")
    return [str(r[0]) for r in cursor.fetchall()]





# CRUD Operations Functions
def add_user():
    name = entry_user.get().strip()
    if not name:
        return messagebox.showwarning("Input Error", "Username required")
    try:
        cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
        conn.commit()
        combo_user['values'] = refresh_users()
        messagebox.showinfo("Success", f"User '{name}' added.")
        entry_user.delete(0, tk.END)
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "User already exists")


def add_project():
    name = entry_project.get().strip()
    if not name:
        return messagebox.showwarning("Input error", "Project name not mentioned") 
    try:
        cursor.execute("INSERT INTO projects (project_name) VALUES (?)", (name,))
        conn.commit()
        combo_project['values'] = refresh_projects()
        messagebox.showinfo("Success", f"Project '{name}' added.")
        entry_project.delete(0, tk.END)
    except sqlite3.IntegrityError:
        return messagebox.showerror("Error", "Project already exists")


def add_issue():
    try:
        proj_id = int(combo_project.get().split(":")[0])
        user_id = int(combo_user.get().split(":")[0])
    except Exception:
        return messagebox.showwarning("Input Error", "Select Project and user")
    
    desc = entry_description.get().strip()
    if not desc:
        return messagebox.showwarning("Input error", "Empty Description")
    
    cursor.execute("INSERT INTO issues (project_id, user_id, description) VALUES (?,?,?)", (proj_id, user_id, desc))
    conn.commit()
    combo_issue_id['values'] = get_issue_ids()
    messagebox.showinfo("Success", "Issue added")
    entry_description.delete(0, tk.END)


def mark_solved():
    try:
        iss_id = int(combo_issue_id.get())
    except ValueError:
        return messagebox.showerror("Error", "Select an Issue ID")
    
    cursor.execute("UPDATE issues SET status='Solved' WHERE issue_id=?", (iss_id,))
    if cursor.rowcount:
        conn.commit()
        combo_issue_id['values'] = get_issue_ids()
        messagebox.showinfo("Updated", "Marked as solved")
    else:
        messagebox.showerror("Error", "Issue ID not found")


def view_issues(filter_sql=None, params=()):
    base = (
        "SELECT i.issue_id, p.project_name, u.name, i.description, i.status "
        "FROM issues i "
        "JOIN projects p ON i.project_id = p.project_id "
        "JOIN users u ON i.user_id = u.user_id "
    )
    sql = base + (f"WHERE {filter_sql}" if filter_sql else "")
    cursor.execute(sql, params)
    rows = cursor.fetchall()
    output.delete('1.0', tk.END)
    if not rows:
        return output.insert(tk.END, "No issues found")
    for r in rows:
        output.insert(tk.END,
                      f"ID:{r[0]} | Project:{r[1]} | User:{r[2]}\n"
                      f" Desc:{r[3]}\n"
                      f" Status:{r[4]}\n"
                    )
        

def export_to_csv():
    cursor.execute(
        "SELECT i.issue_id, p.project_name, u.name, i.description, i.status "
        "FROM issues i "
        "JOIN projects p ON i.project_id = p.project_id "
        "JOIN users u ON i.user_id = u.user_id "
    )
    rows = cursor.fetchall()
    if not rows:
        return messagebox.showinfo("No Data", "No issues to export")
    
    with open("Generated_CSV's/BugTracker.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(['Issue_ID', 'Project', 'User', 'Description', 'Status'])
        writer.writerows(rows)
    messagebox.showinfo("Exported", "Successfully Exported")


def view_by_project():
    pid = int(combo_project.get().split(':')[0])
    view_issues("i.project_id = ?", (pid,))

def view_by_user():
    uid = int(combo_user.get().split(':')[0])
    view_issues("i.user_id = ?", (uid,))


# UI SETUP
root = tk.Tk()
root.title("Bug Tracker")
root.geometry("750x600")

# Frames for layout
top = tk.Frame(root, padx=10, pady=10)
mid = tk.Frame(root, padx=10, pady=10)
bot = tk.Frame(root, padx=10, pady=10)
top.pack(fill='x')
mid.pack(fill='x')
bot.pack(fill='both', expand=True)



# ------------- Top Frame - Add User and Project ---------------------
# ----------> USERS
tk.Label(top, text="Username : ").grid(row=0, column=0, padx=5, pady=5)
entry_user = tk.Entry(top)
entry_user.grid(row=0, column=1, padx=5, pady=5)
tk.Button(top, text="Add User", command=add_user).grid(row=0, column=2, padx=5, pady=5)

# ----------> PROJECTS
tk.Label(top, text="Project Name : ").grid(row=1, column = 0, padx=5, pady=5)
entry_project = tk.Entry(top)
entry_project.grid(row=1, column=1, padx=5, pady=5)
tk.Button(top, text="Add Project", command=add_project).grid(row=1, column=2, padx=5)



# Mid Frame - Issue and Mark Solved 
tk.Label(mid, text="Project : ").grid(row=0, column=0, padx=5, pady=5)
combo_project = ttk.Combobox(mid, values=refresh_projects(), state='readonly')
combo_project.grid(row=0, column=1, padx=5, pady=5)


tk.Label(mid, text="User:").grid(row=1, column=0, padx=5, pady=5)
combo_user = ttk.Combobox(mid, values=refresh_users(), state='readonly')
combo_user.grid(row=1, column=1)

tk.Label(mid, text="Description:").grid(row=2, column=0, padx=5, pady=5)
entry_description = tk.Entry(mid, width=50)
entry_description.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

tk.Button(mid, text="Add Issue", command=add_issue).grid(row=3, column=0, padx=5, pady=5)

tk.Label(mid, text="Issue ID:").grid(row=3, column=1, padx=5)
combo_issue_id = ttk.Combobox(mid, values=get_issue_ids(), state='readonly', width=10)
combo_issue_id.grid(row=3, column=2, padx=5)
tk.Button(mid, text="Mark Solved", command=mark_solved).grid(row=3, column=3, padx=5)


# VIEW BUTTONS
tk.Button(mid, text="View all issues", command=lambda: view_issues()).grid(row=4, column=0, pady=10)
tk.Button(mid, text="View Solved", command=lambda: view_issues("i.status='Solved'")).grid(row=4, column=1)
tk.Button(mid, text="View Unsolved", command=lambda: view_issues("i.status='unsolved'")).grid(row=4, column=2)
tk.Button(mid, text="View by Project", command=view_by_project).grid(row=5, column=0)
tk.Button(mid, text="View by User", command=view_by_user).grid(row=5, column=1)
tk.Button(mid, text="Export CSV", command=export_to_csv).grid(row=5, column=2)


# Bottom Frame: Output Display
output = tk.Text(bot, wrap='word')
output.pack(fill='both', expand=True)

def on_close():
    conn.close()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()