import sqlite3
import csv

conn = sqlite3.connect('Databases/course_Reg.db')
cursor = conn.cursor()

# Create table for students
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students(
               student_id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL
               )
''')

# Create table for courses
cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses(
               course_id INTEGER PRIMARY KEY AUTOINCREMENT,
               course_name TEXT NOT NULL)
''')

# Create table for connecting students and courses
cursor.execute('''
    CREATE TABLE IF NOT EXISTS enrollments(
               student_id,
               course_id,
               PRIMARY KEY (student_id, course_id),
               FOREIGN KEY (student_id) REFERENCES students(student_id),
               FOREIGN KEY (course_id) REFERENCES courses(course_id))
''')
conn.commit()



# CORE FUNCTIONS
def add_Student():
    name = input("Enter Name :- ")
    cursor.execute("INSERT INTO students (name) VALUES (?)", (name,))
    conn.commit()
    print("Student added to database.")

def add_course():
    course_name = input("Enter Course Name :- ")
    cursor.execute("INSERT INTO courses (course_name) VALUES (?)", (course_name,))
    conn.commit()
    print("Courses added to database")

def enroll_Students():
    # Show all students
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    print("\nStudents : ")
    for eachStudent in students:
        print(f"{eachStudent[0]} : {eachStudent[1]}")
    
    # Get student ID
    sid = int(input("\nEnter Student ID :- "))

    # Show all courses
    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()
    print("\nCourses : ")
    for eachCourse in courses:
        print(f"{eachCourse[0]} : {eachCourse[1]}")
    
    # Get course ID
    cid = int(input("Enter Course ID : "))

    # Insert into elements
    try:
        cursor.execute("INSERT INTO enrollments VALUES (?,?)", (sid, cid))
        conn.commit()
        print("Enrollment Sucessful")

    except sqlite3.IntegrityError as e:
        print("Error : ", e)

# View all courses using join
def view_courses():
    cursor.execute('''
        SELECT s.name, c.course_name
        FROM students s
        LEFT JOIN enrollments e ON s.student_id = e.student_id
        LEFT JOIN courses c ON e.course_id = c.course_id
        ORDER BY s.name
    ''')
    results = cursor.fetchall()

    if not results:
        print("No students or enrollments found.")
        return

    from collections import defaultdict

    student_courses = defaultdict(list)
    for student_name, course_name in results:
        student_courses[student_name].append(course_name if course_name else "[No Enrollments]")

    print("\n📋 Students and Their Courses:")
    for student, courses in student_courses.items():
        print(f"\n{student}:")
        for course in courses:
            print(f"  - {course}")
    print()



def delete_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    print("\nStudents : ")
    for s in students:
        print(f"{s[0]} : {s[1]}")
    
    sid = int(input("Enter ID to delete : "))

    # Delete
    cursor.execute('DELETE FROM enrollments WHERE student_id = ?', (sid,))
    cursor.execute('DELETE FROM students WHERE student_id = ?', (sid,))
    conn.commit()
    print(f"Student with ID '{sid}' Deleted ")


def enrollmentsToCsv():
    cursor.execute('''
        SELECT s.name AS student_name, c.course_name AS course_name
                   FROM enrollments e
                   JOIN students s ON e.student_id = s.student_id
                   JOIN courses c ON e.course_id = c.course_id
    ''')
    records = cursor.fetchall()
    
    with open("Generated_CSV's/Course_Enrollments.csv", 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Student Name', 'Course Name'])
        writer.writerows(records)
    
    print("Generated Successfully !!!")


# CLI Interface
def main():
    while True:
        print("""
======== 🎓 Course Registration System ========
1. Add Student
2. Add Course
3. Enroll Student in Course
4. View Student's Courses
5. Delete Students
6. Export Enrollments
7. Exit
""")
        choice = input("Enter Choice : ")

        if choice == '1':
            add_Student()

        elif choice == '2':
            add_course()
        
        elif choice == '3':
            enroll_Students()

        elif choice == '4':
            view_courses()

        elif choice == '5':
            delete_students()

        elif choice == '6':
            enrollmentsToCsv()

        elif choice == '7':
            print("Closed....")
            conn.close()
            break

        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()


