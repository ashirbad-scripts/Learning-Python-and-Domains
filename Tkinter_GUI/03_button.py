import tkinter as tk

root = tk.Tk()
root.title("Learning Buttons")
root.geometry("400x300")

# Function to call a button when clicked
def onCall():
    print("Button was clicked")

button = tk.Button(root, text="Click Me", command=onCall)
button.pack()

root.mainloop()
