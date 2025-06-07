# Write a try/except block to handle division by zero.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("cant divide by zero")

# Handle a file not found error when opening a file.
try: 
    with open("dummy.txt", 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("file not found")

# Handle a ValueError when converting a string to integer.
try: 
    num = int('abc')
except ValueError:
    print("Invalid conversion")

# Use `else` with try/except when no exception occurs.
try: 
    num = int("42")
except ValueError:
    print("Failed")
else:
    print("successful ", num)

# Use `finally` to always print "Execution finished" after try/except.
try:
    num = 10 / 0
except ZeroDivisionError:
    print("cant divide by zero")
finally:
    print("Execution finished")

# Catch multiple exceptions with a single except block.
try: 
    x = int('abc')
    y = 10 / 2
except (ValueError, ZeroDivisionError):
    print("some error")
finally:
    print("Execut.. completed")

# Catch different exceptions separately with multiple except blocks.
try:
    print(5 / 0)
except ValueError:
    print("Cuaght value error")
except ZeroDivisionError:
    print("Zero Division error")

# Raise a ValueError manually if a negative number is entered.
try:
    result = (5 / 0)
    if result < 0:
        raise ValueError("Negative numebr")
    else:
        raise ZeroDivisionError("cant be divided by zero")
except ZeroDivisionError as e:
    print("error caught", e)


# Write a function that handles user input errors properly.
def getInteger():
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("You entered a string")
    else:
        print("You entered ", num)

getInteger()

#  Wrap file read operations inside try/except/finally.
try:
    file = open("dummy.txt", "r")
    content = file.read()
    print(content)

except FileNotFoundError:
    print("File was not found")

finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("File closed")


# Write a list of numbers to a file and print one number per line
numbers = [1,2,3,4,5]
with open("Level_6/numbers.txt", "w") as f:
    for eachNum in numbers:
        f.write(str(eachNum) + "\n")
print("Numbers written")


# Use of o check if a file exists before printing it
import os
filename = "Level_6/numbers.txt"
if os.path.exists(filename):
    with open(filename, "r") as f:
        print(f.readlines())
else:
    print("File not found")


# Create a file copy utility: copy content from one file to another
with open("Level_6/example.txt", "r") as src:
    content = src.readlines()

with open("Level_6/b.txt", "w") as target:
    target.writelines(content)

print("Content copied successfully")