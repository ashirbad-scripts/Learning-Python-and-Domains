import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("Simple Calculator")

# Input fields
entry1 = tk.Entry(root)
entry1.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

# result label
resultLabel = tk.Label(root, text="Result : ")
resultLabel.pack(pady=10)

# operations
def add():
    try:
        res = float(entry1.get()) + float(entry2.get())
        resultLabel.config(text=f"Result : {res}", fg="green", font=("Consolas", 12))

    
    except ValueError as e:
        resultLabel.config(text=f"Error message:  {e}", fg="red")

def subtract():
    try:
        res = float(entry1.get()) - float(entry2.get())
        resultLabel.config(text=f"Result : {res}", fg="green", font=("Consolas", 12))
    
    except ValueError:
        resultLabel.config(text=f"{ValueError}", fg="red")


def multiply():
    try:
        res = float(entry1.get()) * float(entry2.get())
        resultLabel.config(text=f"Result : {res}", fg="green", font=("Consolas", 12))
    
    except ValueError as e:
        resultLabel.config(text=f"Error Message : {e}", fg="red")


def divide():
    try: 
        res = float(entry1.get()) / float(entry2.get())
        resultLabel.config(text=f"Result : {res}", fg="green", font=("Consolas", 12))
    
    except ZeroDivisionError as err:
        resultLabel.config(text=f"Error message {err}", fg="red")
    
    except ValueError as e:
        resultLabel.config(text=f"Error message: {e}", fg="red")


# Creating buttons
tk.Button(root, text="add", command=add).pack()
tk.Button(root, text="subtract", command=subtract).pack()
tk.Button(root, text="multiply", command=multiply).pack()
tk.Button(root, text="divide", command=divide).pack()



root.mainloop()