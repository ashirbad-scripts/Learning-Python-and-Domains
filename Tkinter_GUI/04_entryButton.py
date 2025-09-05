import tkinter as tk

root = tk.Tk()
root.title("Entry Button")
root.geometry("400x300")

# Create an entry widget
entry = tk.Entry(root, width=30)
entry.pack()

# Function to print "entered text"
def showText():
    userInput = entry.get()
    print("You typed: ", userInput)

# Button to trigger input
button = tk.Button(root, text="Print Text", command=showText)
button.pack()

root.mainloop()