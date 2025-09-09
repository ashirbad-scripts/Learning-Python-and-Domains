
# =================== BASIC VERSION =================
# import tkinter as tk

# root = tk.Tk()
# root.title("")
# root.geometry("400x300")

# # label
# label = tk.Label(root, text="Change my color", font=("Arial", 16))
# label.pack(pady=20)


# # function to change label color
# def changeColor():
#     label.config(fg="green")

# # Button
# button = tk.Button(root, text="change color", command=changeColor)
# button.pack(pady=10)

# root.mainloop()



# =================== ADVANCE VERSION =================
import tkinter as tk

class colorChangeApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300")

        # Create label
        self.colorLabel = tk.Label(self.root, text="Change color", font=("Arial", 16))
        self.colorLabel.pack(pady=10)

        # Cretae button
        self.button = tk.Button(self.root, text="change", command=self.changeColor)
        self.button.pack()

        # Reset button
        self.resetButton = tk.Button(self.root, text="Reset Color", command=self.resetColor).pack(pady=10)

    
    def changeColor(self):
        self.colorLabel.config(fg="green")
    
    def resetColor(self):
        self.colorLabel.config(fg="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = colorChangeApp(root)
    root.mainloop()
    