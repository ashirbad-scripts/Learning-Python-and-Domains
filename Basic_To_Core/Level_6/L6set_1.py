# Open a text file in write mode and write "Hello, Python!" to it.

# RULE - 101 - MAINTAIN DIRECTORY
'''
IF YOU ARE OPEING lEVEL_6/... THEN LEVEL 6 MUST BE IN ROOT DIRECTORY ONLY
LIKE PYTHON>LEVEL6/....

IT WONT WORK :-
JS
PYTHON/lEVEL_6/.....

MAKE SURE YOUR OPEING FOLDER IS ONLY IN ROOT DIRECTORY 

'''

file = open("Level_6/example.txt", "w")
file.write("Hello file")
file.close()

# Open a file in read mode and print its contents.
file = open("Level_6/example.txt", "r")
print(file.read())
file.close()

# Open a file in append mode and add a new line.
file = open("Level_6/example.txt", "a")
file.write("\n this is a new line")
file.close()

# Write a list of 5 names into a file, each on a new line.
names = ["Alice", "Bob", "Charlie", "David", "Eva"]
file = open("Level_6/example.txt", "w")
for eachName in names:
    file.write(eachName + "\n")
file.close()


# Read only the first 10 characters from a file.
# file should not be empty
file = open("Level_6/example.txt", "r")
print(file.read(10))
file.close()

# Read a file line by line using a loop.
file = open("Level_6/example.txt", "r")
for eachLine in file:
    print(eachLine.strip())
file.close()


# Write user input to a new file.
userInput = input("Enter something: ")
file = open("Level_6/example.txt", "w")
file.write(userInput)
file.close()

# Count the number of lines in a text file.
file = open("Level_6/example.txt", "r")
lines = file.readlines()
print("Numebr of lines are : ", len(lines))
file.close()

# Overwrite a file completely with new content.
file = open("Level_6/example.txt", "w")
file.write("this is a new content")
file.close()


#  Close a file manually and check if it's closed.---
file = open("Level_6/example.txt", "r")
print(file.closed)
file.close()
print(file.closed)
