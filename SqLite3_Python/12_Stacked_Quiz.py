import sqlite3
import random
import datetime
import csv

DB_File = "Databases/Quiz.db"
CSV_Path = "Generated_CSV's/quiz.csv"

# Connection
conn = sqlite3.connect(DB_File)
cursor = conn.cursor()

# Create tables
def init_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            is_admin INTEGER NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses(
            course_id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT NOT NULL UNIQUE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions(
            q_id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_id INTEGER NOT NULL,
            level TEXT NOT NULL CHECK(level IN ('basic','advanced')),
            question_text TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            correct_option TEXT NOT NULL CHECK(correct_option IN ('A','B','C','D')),
            FOREIGN KEY (course_id) REFERENCES courses(course_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attempts(
            attempt_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            course_id INTEGER NOT NULL,
            level TEXT NOT NULL,
            score INTEGER NOT NULL,
            total INTEGER NOT NULL,
            taken_at TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(user_id),
            FOREIGN KEY (course_id) REFERENCES courses(course_id)
        )
    ''')
    conn.commit()

# User functions
def register_user():
    name = input("Enter Name: ").strip()
    if not name:
        print("Username cannot be empty\n")
        return
    is_admin = 1 if name.startswith('A1875_') else 0

    try:
        cursor.execute("INSERT INTO users (name, is_admin) VALUES (?, ?)", (name, is_admin))
        conn.commit()
        print(f"User '{name}' registered.\n")
    except sqlite3.IntegrityError:
        print("Username already exists.\n")

def login_user():
    name = input("Enter Name: ").strip()
    cursor.execute("SELECT user_id, is_admin FROM users WHERE name = ?", (name,))
    row = cursor.fetchall()
    if row:
        user_id, is_admin = row[0]
        print(f"Welcome, {name}!\n")
        return {'user_id': user_id, 'name': name, 'is_admin': is_admin}
    print(f"User '{name}' not found, please register first.\n")
    return None

# Course and question management
def add_course():
    cname = input("Course name: ").strip()
    if not cname:
        print("Enter course name.\n")
        return
    try:
        cursor.execute("INSERT INTO courses (course_name) VALUES (?)", (cname,))
        conn.commit()
        print("Course added.\n")
    except sqlite3.IntegrityError:
        print("Course already exists.\n")

def list_course():
    cursor.execute("SELECT * FROM courses")
    return cursor.fetchall()

def add_question():
    courses = list_course()
    if not courses:
        print("Add a course first.\n")
        return
    print("Courses:")
    for cid, cn in courses:
        print(f"{cid}. {cn}")
    try:
        cid = int(input("Select Course ID: "))
    except ValueError:
        print("Invalid input.\n")
        return

    lvl = input("Level (basic/advanced): ").strip().lower()
    if lvl not in ('basic', 'advanced'):
        print("Invalid level.\n")
        return

    qtext = input("Question: ").strip()
    opts = [input(f"Option {ch}: ").strip() for ch in ['A', 'B', 'C', 'D']]
    corr = input("Correct Option (A/B/C/D): ").strip().upper()
    if corr not in ('A', 'B', 'C', 'D'):
        print("Invalid correct option.\n")
        return

    cursor.execute(
        "INSERT INTO questions (course_id, level, question_text, option_a, option_b, option_c, option_d, correct_option)"
        " VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (cid, lvl, qtext, opts[0], opts[1], opts[2], opts[3], corr)
    )
    conn.commit()
    print("Question added.\n")

# Viewing and exporting
def view_questions():
    courses = list_course()
    if not courses:
        print("No courses found.\n")
        return
    for cid, cn in courses:
        print(f"{cid}. {cn}")
    try:
        cid = int(input("Course ID: "))
    except ValueError:
        print("Invalid input.\n")
        return
    lvl = input("Level (basic/advanced): ").strip().lower()
    cursor.execute("SELECT q_id, question_text, correct_option FROM questions WHERE course_id = ? AND level = ?", (cid, lvl))
    rows = cursor.fetchall()
    if not rows:
        print("No questions found.\n")
        return
    for qid, qt, corr in rows:
        print(f"{qid}. {qt} (Answer: {corr})")
    print()

def view_attempts():
    cursor.execute("SELECT attempt_id, user_id, course_id, level, score, total, taken_at FROM attempts")
    rows = cursor.fetchall()
    for r in rows:
        print(f"ID:{r[0]} User:{r[1]} Course:{r[2]} Level:{r[3]} Score:{r[4]}/{r[5]} At:{r[6]}")
    print()

def export_to_csv(table, CSV_Path, header):
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    if not rows:
        print(f"No data to export from '{table}'.\n")
        return
    with open(CSV_Path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)
    print(f"Data exported to '{CSV_Path}'\n")

# Quiz flow
def take_quiz(user_id):
    courses = list_course()
    if not courses:
        print("No courses found.\n")
        return
    for cid, cn in courses:
        print(f"{cid}. {cn}")
    try:
        cid = int(input("Course ID: "))
    except ValueError:
        print("Invalid course ID.\n")
        return
    lvl = input("Level (basic/advanced): ").strip().lower()
    cursor.execute("SELECT q_id FROM questions WHERE course_id = ? AND level = ?", (cid, lvl))
    qs = cursor.fetchall()
    if not qs:
        print("No questions available.\n")
        return
    random.shuffle(qs)
    total = min(5, len(qs))
    score = 0

    for i, (qid,) in enumerate(qs[:total], 1):
        cursor.execute("SELECT question_text, option_a, option_b, option_c, option_d, correct_option FROM questions WHERE q_id = ?", (qid,))
        qt, a, b, c, d, correct = cursor.fetchone()
        print(f"\nQ{i}: {qt}")
        print(f"A. {a}")
        print(f"B. {b}")
        print(f"C. {c}")
        print(f"D. {d}")
        ans = input("Answer: ").strip().upper()
        if ans == correct:
            score += 1

    print(f"\nScore: {score}/{total}\n")

    cursor.execute(
        "INSERT INTO attempts (user_id, course_id, level, score, total, taken_at) VALUES (?, ?, ?, ?, ?, ?)",
        (user_id, cid, lvl, score, total, datetime.datetime.now().isoformat())
    )
    conn.commit()

# Menus
def admin_menu():
    while True:
        print("""
Admin Menu:
1) Add Course
2) Add Question
3) View Questions
4) View Attempts
5) Export Questions
6) Export Attempts
0) Logout
""")
        ch = input("Choice: ").strip()
        if ch == '1': add_course()
        elif ch == '2': add_question()
        elif ch == '3': view_questions()
        elif ch == '4': view_attempts()
        elif ch == '5':
            export_to_csv('questions', "Generated_CSV's/12_QUIZ/questions.csv",
                ['q_id', 'course_id', 'level', 'question_text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_option'])
        elif ch == '6':
            export_to_csv('attempts', "Generated/CSV's/12_QUIZ/attempts.csv",
                ['attempt_id', 'user_id', 'course_id', 'level', 'score', 'total', 'taken_at'])
        elif ch == '0': break
        else: print("Invalid choice.\n")

def user_menu(user):
    while True:
        print("""
User Menu:
1) Take Quiz
0) Logout
""")
        ch = input("Choice: ").strip()
        if ch == '1':
            take_quiz(user['user_id'])
        elif ch == '0':
            break
        else:
            print("Invalid choice.\n")

# Main
def main():
    init_db()
    while True:
        print("""
1) Register
2) Login
0) Exit
""")
        ch = input("Choice: ").strip()
        if ch == '1':
            register_user()
        elif ch == '2':
            user = login_user()
            if user:
                if user['is_admin']:
                    admin_menu()
                else:
                    user_menu(user)
        elif ch == '0':
            break
        else:
            print("Invalid choice.\n")
    conn.close()

if __name__ == "__main__":
    main()
