import sqlite3
import csv

conn = sqlite3.connect("Databases/Employee_Management.db")
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS departments (
               dept_id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL)
''')

# Create employees table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
               emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               dept_id INTEGER,
               FOREIGN KEY (dept_id) REFERENCES departments(dept_id))
''')

# Projects table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS projects (
               proj_id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL)
''')


# Assignments table. (link emp to projects)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS assignments(
               emp_id INTEGER,
               proj_id INTEGER,
               PRIMARY KEY (emp_id, proj_id),
               FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
               FOREIGN KEY (proj_id) REFERENCES projects (proj_id))
''')

conn.commit()


# --------------- FUNCTIONS ------------
def add_department():
    name = input("Enter department name : ")
    try:
        cursor.execute("INSERT INTO departments (name) VALUES (?)", (name,))
        conn.commit()
        print("Department added Successfully")
    
    except sqlite3.IntegrityError as e:
        print("Error Message : ", e)




def add_employee():
    name = input("Enter employee name : ")

    # Display available departments 
    cursor.execute("SELECT * FROM departments")
    depts = cursor.fetchall()
    print("\nDepartments :- ")
    for d in depts:
        print(f"{d[0]} : {d[1]}")
    
    try:
        dept_id = int(input("Enter department ID for employee :- "))
        cursor.execute("INSERT INTO employees (name, dept_id) VALUES (?,?)", (name, dept_id))
        conn.commit()
        print("Employee added to department")
    
    except:
        print("Invalid department \n")



# Add new projects
def add_project():
    name = input("Enter Project name :- ")
    cursor.execute("INSERT INTO projects (name) VALUES (?)", (name,))
    conn.commit()
    print("Project added Successfully")



def assign_employee_to_project():
    # List all employees
    cursor.execute("SELECT * FROM employees")
    emp = cursor.fetchall()
    print("\nEmployees Available :- ")
    for e in emp:
        print(f"{e[0]}. {e[1]}")
    emp_id = int(input("Enter employee ID :- "))


    # List Projects
    cursor.execute("SELECT * FROM projects")
    projects = cursor.fetchall()
    print("\nProjects Available :- ")
    for p in projects:
        print(f"{p[0]}. {p[1]}")
    proj_id = int(input("Enter Project ID :- "))

    # Attempt to assign
    try:
        cursor.execute("INSERT INTO assignments(emp_id, proj_id) VALUES (?,?)", (emp_id, proj_id))
        conn.commit()
        print("Assignment Sucessful")
    
    except sqlite3.IntegrityError as e:
        print("Error : ", e)



def view_employees_by_project():
    cursor.execute("SELECT * FROM projects")
    projects = cursor.fetchall()
    print("\nProjects : ")
    for p in projects:
        print(f"{p[0]} {p[1]}")
    proj_id = int(input("Enter project ID :- "))

    cursor.execute('''
        SELECT employees.emp_id, employees.name
                   FROM employees
                   JOIN assignments ON employees.emp_id = assignments.emp_id
                   WHERE assignments.proj_id = ?
    ''', (proj_id,))

    results = cursor.fetchall()
    if results: 
        print("\nEmployees in projects are :- ")
        for r in results:
            print(f"- {r[0]} : {r[1]}")
    
    else:
        print("No employees under this project")




# Export to csv
def exportToCsv():
    cursor.execute('''
        SELECT employees.name, projects.name
                   FROM assignments
                   JOIN employees ON assignments.emp_id = employees.emp_id
                   JOIN projects ON assignments.proj_id = projects.proj_id
    ''')
    rows = cursor.fetchall()
    with open("Generated_CSV's/Employee_Projects.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(['Employee Name', 'Project Name'])
        writer.writerows(rows)
    print("File Generated Successfully !!!!!!")



# CLI MENU
def main():
    while True:
                print("""
========= 🧑‍💼 EMPLOYEE MANAGEMENT SYSTEM =========
1. Add Department
2. Add Employee
3. Add Project
4. Assign Employee to Project
5. View Employees by Project
6. Export All Assignments to CSV
7. Exit
""")
                choice = input("Enter Choice :- ")

                if choice == '1':
                    add_department()
                
                elif choice == '2':
                    add_employee()
                
                elif choice == '3':
                    add_project()
                
                elif choice == '4':
                    assign_employee_to_project()
                
                elif choice == '5':
                    view_employees_by_project()
                
                elif choice == '6':
                    exportToCsv()
                
                elif choice == '7':
                    print("Closed......")
                    conn.close()
                    break
                
                else:
                    print("Invalid Choice")

if __name__ == "__main__":
    main()