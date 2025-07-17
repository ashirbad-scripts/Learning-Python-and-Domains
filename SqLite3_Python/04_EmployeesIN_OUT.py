import sqlite3
import datetime

conn = sqlite3.connect('Databases/employees.db')
cursor = conn.cursor()

# Create attendance table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id TEXT NOT NULL,
        name TEXT NOT NULL,
        date TEXT NOT NULL,
        check_in TEXT NOT NULL,
        check_out TEXT,
        UNIQUE(employee_id, date)
    )
''')
conn.commit()

# ------------------ Core Functions ------------------

def check_in(employee_id, name):
    today = datetime.date.today().isoformat()
    now = datetime.datetime.now().time().strftime("%H:%M:%S")

    try:
        cursor.execute('''
            INSERT INTO attendance (employee_id, name, date, check_in)
            VALUES (?, ?, ?, ?)
        ''', (employee_id, name, today, now))
        conn.commit()
        print(f"✅ Check-in successful at {now}")
    except sqlite3.IntegrityError:
        print("⚠️ Already checked in today.")

def check_out(employee_id):
    today = datetime.date.today().isoformat()
    now = datetime.datetime.now().time().strftime("%H:%M:%S")

    cursor.execute('''
        SELECT * FROM attendance
        WHERE employee_id = ? AND date = ? AND check_out IS NULL
    ''', (employee_id, today))
    row = cursor.fetchone()

    if row:
        cursor.execute('''
            UPDATE attendance
            SET check_out = ?
            WHERE id = ?
        ''', (now, row[0]))
        conn.commit()
        print(f"✅ Check-out successful at {now}")
    else:
        print("⚠️ No check-in found for today or already checked out.")

def view_today_attendance():
    today = datetime.date.today().isoformat()
    cursor.execute('''
        SELECT employee_id, name, check_in, check_out
        FROM attendance WHERE date = ?
    ''', (today,))
    rows = cursor.fetchall()

    if not rows:
        print("⚠️ No attendance records for today.")
    else:
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, In: {row[2]}, Out: {row[3] or '—'}")

# ------------------ CLI Menu ------------------

def main():
    while True:
        print("\n--- Employee Attendance System ---")
        print("1. Check-In")
        print("2. Check-Out")
        print("3. View Today's Attendance")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == '1':
            eid = input("Employee ID: ")
            name = input("Employee Name: ")
            check_in(eid, name)

        elif choice == '2':
            eid = input("Employee ID: ")
            check_out(eid)

        elif choice == '3':
            view_today_attendance()

        elif choice == '4':
            print("👋 Exiting...")
            break

        else:
            print("⚠️ Invalid option. Try again.")

    conn.close()

if __name__ == "__main__":
    main()