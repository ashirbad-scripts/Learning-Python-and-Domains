import tkinter as tk

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title = "Login Form"
        self.root.geometry("400x300")

        self.build_ui()
    
    def build_ui(self):
        # username
        tk.Label(self.root, text="Username").grid(row=0, column=0, padx=10, pady=10)
        self.username = tk.Entry(self.root)
        self.username.grid(row=0, column=1, padx=10, pady=10)

        # password
        tk.Label(self.root, text="Password").grid(row=1, column=0, padx=10, pady=10)
        self.password = tk.Entry(self.root, show="*")
        self.password.grid(row=1, column=1, padx=10, pady=10)

        # Login Button
        button = tk.Button(self.root, text="login", command=self.login)
        button.grid(row=2, column=0, columnspan=2, pady=10)

        # Result Label
        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def login(self):
        u = self.username.get()
        p = self.password.get()

        if u == "admin" and p == "1234":
            print("success")
            self.result_label.config(text="Login Successful", fg="green")
        else:
            print("Error")
            self.result_label.config(text="Error Credentials", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
