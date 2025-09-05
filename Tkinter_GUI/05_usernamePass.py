import tkinter as tk

root = tk.Tk()
root.title("")
root.geometry("400x300")

# Username label and entry
username_label = tk.Label(root, text="Username: " )
username_label.grid(row=0, column=0, padx=10, pady=10)

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)


# Password label and entry
password_label = tk.Label(root, text="Password: ")
password_label.grid(row=1, column=0)

password_entry = tk.Entry(root)
password_entry.grid(row=1, column=1)


# # trial version (SELF)
# # Username label and entry
# username_label = tk.Label(root, text="Username: " )
# username_label.grid(row=0, column=0, padx=10, pady=10)

# username_entry = tk.Entry(root)
# username_entry.grid(row=1, column=0, padx=10)


# # Password label and entry
# password_label = tk.Label(root, text="Password: ")
# password_label.grid(row=2, column=0, pady=10)

# password_entry = tk.Entry(root)
# password_entry.grid(row=3, column=0, padx=10)



root.mainloop()