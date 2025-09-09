import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x300")

agree = tk.IntVar()

checkBtn = tk.Checkbutton(root, text="I agree", variable=agree)
checkBtn.pack(pady=10)

def submit():
    if agree.get() == 1:
        print("Form Submitted")
    else:
        messagebox.showwarning("Warning","You must agree")

tk.Button(root, text="Submit", command=submit).pack()

root.mainloop()