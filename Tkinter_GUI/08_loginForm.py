import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

# Username label
tk.Label(root, text="Username").grid(row=0, column=0, pady=5)
username = tk.Entry(root)
username.grid(row=0, column=1)

# Password label and entry
tk.Label(root, text="Password").grid(row=1, column=0, pady=5)
password = tk.Entry(root)
password.grid(row=1, column=1)

resultLabel = tk.Label(root, text="verifying")
resultLabel.grid(row=3, column=0,columnspan=2, pady=10)

def login():
    if username.get() == "admin" and password.get() == "1234":
        print("success")
        resultLabel.config(text="Success")
    else:
        print("Error")
        resultLabel.config(text="Error credentials")

button = tk.Button(root, text="Login", command=login)
button.grid(row=2,column=1, pady=10)

root.mainloop()

# CANNOT USE PACK AND GRID IN ONE ROOT