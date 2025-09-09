# import tkinter as tk

# root = tk.Tk()
# root.geometry("400x300")

# # Initializing count
# count = 0

# # Creating label
# label = tk.Label(root, text="Count : 0", font=("Arial", 16))
# label.pack(pady=10)

# # function to increase count
# def increase():
#     global count
#     count += 1
#     label.config(text=f"Count : {count}")

# # Button
# tk.Button(root, text="Click Me", command=increase).pack(pady=10)
# root.mainloop()


# ADVANCE VERSION
import tkinter as tk

class counterApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300")

        self.count = 0

        # label
        self.label = tk.Label(self.root, text="Clicks : 0", font=("Arial", 16))
        self.label.pack(pady=(50,10))

        # Create button
        self.button = tk.Button(self.root, text="Increase", command=self.increase).pack(pady=10)
    
    def increase(self):
        self.count += 1
        self.label.config(text=f"Count : {self.count}")

if __name__ == "__main__":
    root = tk.Tk()
    app = counterApp(root)
    root.mainloop()

