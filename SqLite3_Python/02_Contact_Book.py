import sqlite3
import csv

# CONNECT DATABASE
conn = sqlite3.connect('Databases/contacts.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts(
               name TEXT PRIMARY KEY,
               phone TEXT NOT NULL,
               email TEXT,
               address TEXT
               )
''')
conn.commit()


# CONTACT BOOK FUNCTIONS
def addContact(name, phone, email, address):
    try:
        cursor.execute("INSERT INTO contacts VALUES (?,?,?,?)", (name, phone, email, address))
        conn.commit()
        print("Contact added Successfuly")
    
    except sqlite3.IntegrityError:
        print("Contact name already exists")



def viewContact():
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    if not rows:
        print("No contacts Found")
    else:
        for eachRow in rows:
            print(f"Name : {eachRow[0]}, Phone : +91 {eachRow[1]}, email : {eachRow[2]}, address : {eachRow[3]}")



def searchContact(name):
    cursor.execute("SELECT * FROM contacts WHERE name = ?", (name,))
    row = cursor.fetchone()
    if row:
        for eachRow in row:
            print(eachRow)
        # print(f"Name : {eachRow[0]}, Phone : +91 {eachRow[1]}, email : {eachRow[2]}, address : {eachRow[3]}")
        
    else:
        print("Contacts not found")



def updateContact(name, new_phone, new_email, new_address):
    cursor.execute("""
        UPDATE contacts
                   SET phone = ?, email = ?, address = ?
                   WHERE name = ?
    """, (name, new_phone, new_email, new_address))
    conn.commit()
    if cursor.rowcount == 0:
        print("No Contact with name found")
    else:
        print("Contact updated")




def deleteContact(name):
    cursor.execute("DELETE FROM contacts WHERE name = ?", (name,))
    conn.commit()
    if cursor.rowcount == 0:
        print("Nothing to delete")
    else:
        print("Deleted Successfully")




def exportToCsv(filepath = "Generated_CSV's/ContactBook.csv"):
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    if not rows:
        print("No contacts to export")
    
    with open(filepath, mode='a', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Phone', 'Email', 'Address'])
        writer.writerows(rows)
    
    print(f"Contacts exported to {filepath}")



# -------------------- CLI INTERFACE -----------------------
def main():
    while True:
        print("\n------- Contact Book --------\n")
        print("\n 1. Add Contact")
        print("\n 2. View Contact")
        print("\n 3. Search by Name")
        print("\n 4. Update Contact")
        print("\n 5. Delete Contact")
        print("\n 6. Export Contacts")
        print("\n 7. Exit")

        choice = input("Enter Choice :- ")

        if choice == '1':
            n = input("Enter name :- ")
            p = input("Enter phone number :- ")
            e = input("Email Id :- ")
            a = input("Address :- ")
            addContact(n,p,e,a)
        
        elif choice == '2':
            viewContact()
        
        elif choice == '3':
            n = input("Enter name to search :- ")
            searchContact(n)
        
        elif choice == '4':
            new_n = input("Enter name to update :- ")
            new_p = input("New phone number :- ")
            new_e = input("New Email Id :- ")
            new_a = input("New Address :- ")
            updateContact(new_n, new_p, new_e, new_a)
        
        elif choice == '5':
            name = input("Enter name to delete :- ")
            deleteContact(name)
        
        elif choice == '6':
            exportToCsv()
        
        elif choice == '7':
            print("Contact Book Closed !!!!")
            conn.close()
            break

if __name__ == "__main__":
    main()