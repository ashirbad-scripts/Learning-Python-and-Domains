# List all attributes/functions of the math module using dir().
import math
print("Functions in math module: ")
print(dir(math))


# Use the os module to get the current working directory.
import os
cDir = os.getcwd()
print("\n")
print("CURRENT WORKING DIRECTORY IS :- ", cDir)


# Use the time module to measure how long a function takes to run.
import time
def slowFunction():
    time.sleep(2)  # run after 2 seconds
    return "Finished Execution"

start = time.time()
print(slowFunction())
end = time.time()

print("Execution time: ", end - start, "seconds")
