import tkinter as tk

root = tk.Tk()
root.title("Clear Entry")
root.geometry("400x300")

# Add label to entry widget
entry_label = tk.Label(root, text="Type Here something....")
entry_label.pack(pady=(50, 5))  # 20 above 5 below

# print entry widget
print_entry = tk.Entry(root, width=30)
print_entry.pack(pady=(0, 10))

# function to print text
def printText():
    userInput = print_entry.get()
    print("You typed: ", userInput)

# function to clear text
def clearText():
    print_entry.delete(0, tk.END)  # delete from 0th index to end


# call function to print
print_button = tk.Button(root, text="Print Me", command=printText)
print_button.pack()  #pady already comming from top


# Call function to clear
clear_button = tk.Button(root, text="Clear", command=clearText)
clear_button.pack(pady=10)

root.mainloop()