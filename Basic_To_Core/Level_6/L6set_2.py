# WITH auto-closes the file
# Open and read a file using a `with` statement.
with open("Level_6/example.txt", "r") as file:
    print(file.read())

# After reading a file, move the file pointer back to the beginning.
with open("Level_6/example.txt", "r") as file:
    file.read()
    file.seek(0)   # move pointer back to start
    print(file.read())

# Open a file and read only the first line.
with open("Level_6/example.txt", "r") as file:
    first_line = file.readline()
    print(first_line.strip())

# Open a file and read all lines into a list.
with open("Level_6/example.txt", "r") as file:
    lines = file.readlines()
    print(lines)

# Open a file and find the length of the longest line.
with open("Level_6/example.txt", "r") as file:
    lines = file.readlines()
    longestLine = max(lines, key=len)
    print("longest line is: ", longestLine.strip())
    print("Length of the longest line is: ", len(longestLine.strip()))

# Write multiple lines into a file at once using `writelines()`.
lines = ["first line\n", "Second line\n", "third line\n"]
with open("Level_6/example.txt", "w") as file:
    file.writelines(lines)

# Read a file and ignore empty lines.
with open("Level_6/example.txt", "r") as file:
    for eachLine in file:
        if eachLine.strip():
            print(eachLine.strip())

# Append text at a specific position using seek (bonus challenge).
with open("Level_6/example.txt", "r+") as file:  #r+ means read and write
    file.seek(5)  # move to 5th byte
    file.write("Inserted")


# Check if a file exists before trying to open it (hint: `os.path.exists`).
import os
if os.path.exists("Level_6/example.txt"):
    with open("Level_6/example.txt", "r") as file:
        print(file.read())
else:
    print("file not exits")


#  Open a file in binary mode and read the first 10 bytes.
with open("Level_6/example.txt", "rb") as file:
    bytesData = file.read(10)
    print(bytesData)