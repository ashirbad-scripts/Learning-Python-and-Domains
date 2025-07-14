import csv

# Import and connect to sqlite3
import sqlite3

# Connect to database
conn = sqlite3.connect('Databases/student.db')

# Create a cursor to execute sql commands
cursor = conn.cursor()

# CREATE A TABLE FOR STUDENTS
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students(
            roll_no INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            grade TEXT
        )
''')
# Save the changes
conn.commit()


# ADD STUDENTS
def addStudent(roll_no, name, age, grade):
    cursor.execute("INSERT INTO students VALUES (?,?,?,?)", (roll_no, name, age, grade))
    conn.commit()
    print("Student added successfully")


# VIEW STUDENTS
def viewStudents():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for eachrow in rows:
        print(eachrow)


# SEARCH STUDENTS
def searchStudent(roll_no):
    cursor.execute("SELECT * FROM students WHERE roll_no = ?", (roll_no,))
    result = cursor.fetchone()
    print(result if result else "Student not found")



# UPDATE STUDENTS
def updateStudent(roll_no, name, age, grade):
    cursor.execute("""
        UPDATE students
        SET name = ?, age = ?, grade = ?
        WHERE roll_no = ?
    """, (name, age, grade, roll_no))
    conn.commit()
    print("Student updated")



# DELETE STUDENTS
def deleteStudent(roll_no):
    cursor.execute("DELETE FROM students WHERE roll_no = ?", (roll_no,))
    conn.commit()
    print("Student deleted successfully")


def exportToCsv(filename = "Generated_CSV's/StudentsData.csv"):
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if not rows:
        print("No data to export")
    
    with open(filename, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Roll No., Name", "Age", "Grade"])
        writer.writerows(rows)

    print(f"Data exported to {filename}")



# CLI TO RUN THE SCRIPTS
while True:
    print("\n------- Student Management ------\n")
    print("\n 1. Add Students")
    print("\n 2. View all students")
    print("\n 3. Search Students")
    print("\n 4. Update students")
    print("\n 5. Delete students")
    print("\n 6. Export Data")
    print("\n 7. Exit")

    choice = input("\nEnter Choice : ")
    print("-------------------------------------------------\n")

    if choice == '1':
        r = int(input("Roll NO. :- "))
        n = input("Name :- ")
        a = int(input("Age :- "))
        g = input("Grade :- ")
        addStudent(r,n,a,g)
    
    elif choice == '2':
        viewStudents()
    
    elif choice == '3':
        r = int(input("Enter Roll No. to Search :- "))
        searchStudent(r)
    
    elif choice == '4':
        r = int(input("Roll NO. :- "))
        n = input("Name :- ")
        a = int(input("Age :- "))
        g = input("Grade :- ")
        updateStudent(r,n,a,g)
    
    elif choice == '5':
        r = int(input("Enter Roll No. to delete :- "))
        deleteStudent(r)
    
    elif choice == '6':
        exportToCsv()

    elif choice == '7':
        conn.close()
        break

    else:
        print("Invalid Choice.")