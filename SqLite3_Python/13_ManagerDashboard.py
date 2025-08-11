import sqlite3
import csv
from datetime import datetime

# DATABASE
conn = sqlite3.connect("Databases/ManagerDashboard.db")
cursor = conn.cursor()

# Create a list table
cursor.execute('''
CREATE TABLE IF NOT EXISTS clients(
               client_id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               contact TEXT
               )
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS freelancers(
               fr_id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               contact TEXT,
               tech_specs TEXT,
               availability INTEGER,
               min_salary REAL
               )
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS projects(
               p_id INTEGER PRIMARY KEY AUTOINCREMENT,
               client_id INTEGER NOT NULL,
               project_name TEXT NOT NULL,
               tech_specs TEXT,
               deadline TEXT,
               budget REAL,
               assigned_fr_id INTEGER,
               status TEXT DEFAULT 'unassigned',
               FOREIGN KEY (client_id) REFERENCES clients(client_id),
               FOREIGN KEY (assigned_fr_id) REFERENCES freelancers(fr_id)
               )
''')
conn.commit()


# HELPER FUNCTIONS
def add_client_and_project():
    cname = input("Client Name : ").strip()
    contact = input("Client Contact : ").strip()
    if not cname:
        print("Client name required"); return
    cursor.execute("INSERT INTO clients (name, contact) VALUES (?,?)", (cname, contact))
    client_id = cursor.lastrowid

    pname = input("Project Name : ").strip()
    tech = input("Tech Specifications : ").strip()
    deadline = input("Deadline (YYYY_MM_DD) : ").strip()
    budget = input("Budget : ").strip()
    try:
        budget = float(budget)
    except ValueError:
        print("Invalid budget")
        budget = 0.0
    
    # Insert project
    cursor.execute("INSERT INTO projects (client_id, project_name, tech_specs, deadline, budget) VALUES (?,?,?,?,?)",
                   (client_id, pname, tech, deadline, budget))
    conn.commit()
    print(f"Added client '{cname}' and project '{pname}'")



def add_freelancer():
    name = input("Freelancer Name : ").strip()
    contact = input("Contact : ").strip()
    tech = input("Tech Specs : ").strip()
    avail = input("Availability : ").strip()
    salary = input("Min. Salary : ").strip()
    try:
        avail = int(avail)
    except ValueError:
        print("Invalid availability")
        avail = 0
    try:
        salary = float(salary)
    except ValueError:
        print("Invalid Salary")
        salary = 0.0

    cursor.execute("INSERT INTO freelancers (name, contact, tech_specs, availability, min_salary) VALUES (?,?,?,?,?)",
                   (name, contact, tech, avail, salary))
    conn.commit()
    print(f"Freelancer '{name}' added.")


def view_clients_projects():
    cursor.execute('''
    SELECT p.p_id, c.name, c.contact, p.project_name, p.tech_specs,
                   p.deadline, p.budget, p.status,
                   f.name
    FROM projects p
                   JOIN clients c ON p.client_id = c.client_id
                   LEFT JOIN freelancers f ON p.assigned_fr_id = f.fr_id
    ''')
    rows = cursor.fetchall()
    if not rows:
        print("No Clients projects found"); return
    for r in rows:
        print(f"ID:{r[0]}, Client:{r[1]}, Project:{r[3]}, Tech:{r[4]}, Due:{r[5]}, Budget:{r[6]}, Status:{r[7]}, Freelancer:{r[8]}")

    
def view_freelancer():
    cursor.execute("SELECT * FROM freelancers")
    rows = cursor.fetchall()
    if not rows:
        print("No freelancers found"); return
    for r in rows:
        print(f"ID:{r[0]}  | Name:{r[1]} | Tech:{r[2]} | Avail:{r[3]} | MinSal:{r[4]}")


def assign_freelancers():
    cursor.execute("SELECT p_id, project_name, tech_specs FROM projects WHERE status='unassigned'")
    projs = cursor.fetchall()
    if not projs:
        print("No Unassigned Projects found"); return
    print("Unassigned Projects : ")
    for p in projs:
        print(f"{p[0]} {p[1]} (Tech: {p[2]})")
    pid = int(input("Select Project ID : "))

    # SHOW FREELANCERS MATCHING TECH SPECS
    cursor.execute("SELECT tech_specs FROM projects WHERE p_id=?", (pid,))
    tech = cursor.fetchone()[0]
    cursor.execute(
        "SELECT fr_id, name, availability FROM freelancers WHERE tech_specs LIKE ?",
        (f"%{tech}%",)
    )
    frs = cursor.fetchall()
    if not frs:
        print("No matching freelancers found"); return
    print("Matching Freelancers : ")
    for f in frs:
        print(f"{f[0]} {f[1]} (Avail:{f[2]}h)")
    fid = int(input("Select freelancer ID to assign : "))

    # ASSIGN
    cursor.execute(
        "UPDATE projects SET assigned_fr_id=?, status='Assigned' WHERE p_id=?",
        (fid, pid)
    )
    conn.commit()
    print(f"Assigned freelancer {fid} to project {pid}")



def export_to_csv():
    cursor.execute('''
        SELECT p.p_id, c.name, p.project_name, p.tech_specs,
                   p.deadline, p.budget, p.status, f.name
        FROM projects p
                   JOIN clients c ON p.client_id=c.client_id
                   LEFT JOIN freelancers f ON p.assigned_fr_id=f.fr_id
    ''')
    rows = cursor.fetchall()
    filename = "Generated_CSV's/ManagerDashboard.csv"
    with open(filename, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(['ProjectID', 'Client', 'Project', 'Tech', 'Deadline', 'Budget', 'Status', 'Freelancer'])
        w.writerows(rows)
    print(f"Exported report to {filename}")


# CLI MENU
def main():
    while True:
        print("""
=== Manager Dashboard ===
1) Add Client & Project
2) Add Freelancer
3) View All Clients & Projects
4) View All Freelancers
5) Assign Freelancer to Project
6) Export Report to CSV
7) Exit
""")
        choice  = input("Choice : ").strip()
        if choice == '1': add_client_and_project()
        elif choice == '2': add_freelancer()
        elif choice == '3': view_clients_projects()
        elif choice == '4': view_freelancer()
        elif choice == '5': assign_freelancers()
        elif choice == '6': export_to_csv()
        elif choice == '7': break
        else: print("Invalid choice")
    conn.close()

if __name__ == "__main__":
    main()
