# Read a file that may not exist, and create it if not found.
filename = "sample.txt"
try:
    with open(filename, "r") as file:
        content = file.read()

except FileNotFoundError:
    with open(filename, "w") as file:
        file.write("It now exists")
    print(f"File {filename} created")


# Create a function to read numbers from a file and calculate their sum.
def sumNumbers(filename):
    try:
        with open(filename, "r") as file:
            numbers = file.readlines()
            total = sum(int(eachNum.strip()) for eachNum in numbers)
            return total
    except Exception as e:
        print("ERROR: ", e)
        
print(sumNumbers("Level_6/sum.txt"))


# Try to divide numbers read from a file and handle division errors.
try:
    with open("numbers.txt", "r") as file:
        nums = [int(x.strip()) for x in file.readlines()]
        result = nums[0] / nums[1]
        print("Division result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("Some other error:", e)


# Write a program that asks for a filename and reads it safely.
filename = input("Enter filename: ")
try:
    with open(filename, "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found")

# Create a program that backs up a file (copy contents to a new file).
def backUp(original, backup):
    try:
        with open(original, "r") as file1, open (backup, "w") as file2:
            file2.write(file1.read())
        print(f"Backup created as : {backup}")
    
    except Exception as e:
        print("Error: ", e)

print(backUp("Level_6/example.txt", "Level_6/backup.txt"))


# Catch and log errors into an "error_log.txt" file.
try:
    x = int("abc")

except Exception as e:
    with open("Level_6/Error.txt", "a") as log:
        log.write(str(e) + "\n")
    print("Error logged")


# Handle invalid user input and retry until correct input is given.
while True:
    try:
        num = int(input("Enter a number: "))
        print("You entered: ", num)
        break
    except ValueError:
        print("Invalid input")


# Open multiple files simultaneously and read their contents.
def MultipleFiles(file1_name, file2_name):
    try:
        with open(file1_name, "r") as f1, open(file2_name, "r") as f2:
            print(f"contents of {file1_name} are: {f1.read()}")
            print(f"contents of {file2_name} are: {f2.read()}")
    except FileNotFoundError as e:
        print("Error: ", e)
MultipleFiles("Level_6/example.txt", "Level_6/sum.txt")


# Write a program that tries to delete a file and handles permission 
# errors.
import os 
fileToDelete = "Level_6/deleteme.txt"

try:
    os.remove(fileToDelete)
    print(f"{fileToDelete} sucessfully deleted")

except PermissionError as z:
    print("You dont have permission", z)

except FileNotFoundError as e:
    print("File not exist")
    print("Exact reason: ", e)


#  Create a program that reads JSON content from a file and handles parsing errors.
import json

try:
    with open("Level_6/data.json", "r") as file:
        data = json.load(file)
        print(data)

except json.JSONDecodeError:
    print("Error decoding")

except FileNotFoundError:
    print("FIle not found ")


# Advance lesson create a .txt file and then delete it
import os
fileToDelete = "Level_6/DeleteMe.txt"

with open(fileToDelete, 'w') as file:
    file.write("Yo YO willow the isekai")

try:
    with open(fileToDelete, 'r') as file:
        print(f"{fileToDelete} contents is {file.read()}")
    os.remove(fileToDelete)
    print(f"{fileToDelete} deleted completely")

except PermissionError as e:
    print("Error is : ", e)

except FileNotFoundError as e:
    print("Erro is : ", e)



# Advance lesson create a .json file and then delete it
import os
import json

fileToHandle = "Level_6/dummyjson.json"
data = {"message" : "just a dummy file"}

with open(fileToHandle, "w") as file:
    json.dump(data, file)

try:
    os.remove(fileToHandle)
    print(f"{fileToHandle} deleted completed")

except PermissionError as e:
    print("Error: ", e)

except FileNotFoundError as e:
    print("Error: ", e)







# ADVANCE JSON CRUD OPERATIONS
import os
import json

file_path = "Level_6/CRUD.json"


# --- CREATE ---
def create_json():
    data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)
    print("File created with initial data.")
create_json()

# --- READ ---
def read_json():
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        print("Data read from file:")
        print(json.dumps(data, indent=4))
    except FileNotFoundError:
        print("File does not exist. Cannot read.")

# --- UPDATE ---
def update_json():
    try:
        with open(file_path, 'r+') as f:
            data = json.load(f)
            # Update data
            data["age"] = 31
            data["country"] = "USA"
            # Move the file pointer to the beginning before writing
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
        print("File updated successfully.")
    except FileNotFoundError:
        print("File does not exist. Cannot update.")

# --- DELETE ---
def delete_json():
    try:
        os.remove(file_path)
        print("File deleted successfully.")
    except FileNotFoundError:
        print("File already deleted or does not exist.")
    except PermissionError as e:
        print("No permission to delete the file:", e)

# --- MAIN EXECUTION FLOW ---
if __name__ == "__main__":  #NOt mandatory, but prevent file from running when it is imported elsewhere
    create_json()
    read_json()
    update_json()
    read_json()
    delete_json()
    read_json()  # Should fail
