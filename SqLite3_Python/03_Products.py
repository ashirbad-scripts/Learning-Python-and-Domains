import csv
import sqlite3

conn = sqlite3.connect('Databases/products.db')
cursor = conn.cursor()

# CREATE TABLE
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products(
               p_id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               price INTEGER
            )
''')
conn.commit()

# ADD PRODUCTS
def addProducts(p_id, name, price):
    cursor.execute("INSERT INTO products VALUES (?,?,?)", (p_id, name, price))
    conn.commit()
    print("Products added successfully\n")


# VIEW PRODUCTS
def viewProducts():
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    for eachRow in rows:
        print(f"Prouct ID :  {eachRow[0]}, Product Name : {eachRow[1]}, Product Price : {eachRow[2]}")


def searchProduct(p_id):
    cursor.execute("SELECT * FROM products WHERE p_id = ?", (p_id,))
    rows = cursor.fetchone()
    if rows:
        print(f"Product ID: {rows[0]}, Name: {rows[1]}, Price: {rows[2]}")
    else:
        print("Not Found")

def updateProducts(p_id, name, price):
    cursor.execute("""
        UPDATE products
                   SET name = ?, price = ?
                   WHERE p_id = ?
    """, (name, price, p_id))
    conn.commit()
    if cursor.rowcount == 0:
        print("No Poducts found")
    else:
        print("PRoducts Updated")

def deleteProduct(p_id):
    cursor.execute("DELETE FROM products WHERE p_id = ?", (p_id,))
    conn.commit()
    print("Deleted Succcesfully")

def exportToCSV(filepath = "Generated_CSV's/Products.csv"):
    cursor.execute("SELECT * FROM products")
    row = cursor.fetchall()
    if not row:
        print("Nothing Found !!!")
    
    with open(filepath, mode='a', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(['P_ID, P_Name, P_Price'])
        writer.writerows(row)

    print(f"Products exported to '{filepath}'")





# CLI INTERFACE
def main():
    while True:
        print("\n------ Product Management -------\n")
        print("\n 1. Add Product")
        print("\n 2. View Products")
        print("\n 3. Search Products")
        print("\n 4. Update Products")
        print("\n 5. Delete Products")
        print("\n 6. Export")
        print("\n 7. EXIT")

        choice = input("Enter Choice :- ")

        if choice == '1':
            pid = int(input("Enter ID:- "))
            n = input("Enter Name :- ")
            p = int(input("Enter Price :- "))
            addProducts(pid, n, p)
        
        elif choice == '2':
            viewProducts()
        
        elif choice == '3':
            i = int(input("Enter ID to search :- "))
            searchProduct(i)

        elif choice == '4':
            pid = int(input("Enter ID:- "))
            n = input("Enter Name :- ")
            p = int(input("Enter Price :- "))
            updateProducts(pid, n, p)

        elif choice == '5':
            pid = int(input("Enter ID to delete :- "))
            deleteProduct(pid)
        
        elif choice == '6':
            exportToCSV()
        
        elif choice == '7':
            print("Database Closed")
            conn.close()
            break
    
if __name__ == "__main__":
    main()