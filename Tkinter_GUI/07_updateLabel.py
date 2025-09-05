import tkinter as tk

root = tk.Tk()
root.title("")
root.geometry("400x300")

# Create label
label = tk.Label(root, text="Original Text", font=("Arial", 16))
label.pack(pady=20)

# Update Label
def updateLabel():
    label.config(text="Hey, this was updated")

# button to call
button = tk.Button(root, text="Update", command=updateLabel)
button.pack(pady=10) 

root.mainloop()