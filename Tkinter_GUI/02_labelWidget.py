import tkinter as tk

root = tk.Tk()
root.title("Label Example")
root.geometry("400x300")

# Create a label with text
label = tk.Label(root, text="Welcome to Python GUI", font=("Arial", 14))

# Display label
label.pack()

# Place the label in center
# label.pack(expand=True)

root.mainloop()