# Create a function and print a variable defined inside it 
# (local scope).
def greet():
    message = "Hello world"
    print(message)
greet()

# Create a global variable and access it inside a function.
name = "john"
def sayHi():
    print(f"Hi {name}")
sayHi()

# Difference
def sayHi(name):
    print(f"Hello, {name}")
sayHi(name)


# Try modifying a global variable inside a function (without global keyword).
count = 10

def updateCount():
    count = 5
    print(f"Inside count : {count}")

updateCount()
print(f"Outside count: {count}")


# Use global keyword to modify a global variable.
score = 5
print("Original Score: ",score)

def increaseScore():
    global score
    score = score + 10

increaseScore()
print("New Score: ",score)


# Write a function that defines a local variable with same name 
# as global.
name = "john"

def localVar():
    name = "alice"
    print(f"inside: {name}")

localVar()
print(f"Outside name: {name}")


# Show an example of variable shadowing in functions.
x = 50

def shadow():
    x = 100  # Local x shadows the global x
    print("Inside:", x)

shadow()
print("Outside:", x)  # Still 50


# Create two functions — one modifies a variable, the other reads it — observe scope behavior.
value = 5

def modify():
    global value
    value += 10

def read():
    print(f"Current value : {value}")

modify()
read()


# Create nested functions and access outer function’s variables 
# from the inner one.
def outer():
    msg = "Outer message"

    def inner():
        print("Inner accressing: ", msg)
    
    inner()
outer()


# Use a counter inside a function that persists across calls 
# (hint: default arg or global).
count = 0

def increment():
    global count
    count += 10
    return count

# increment()
# print(count)
print(increment())
print(increment())


#  Demonstrate how variable scope works during recursion.
def countdown(n):
    if n == 0:
        print("Blast Off")
    else:
        print("Counting: ", n)
        countdown(n - 1)

userInput = int(input("Enter countdown value: "))
countdown(userInput)
