# Write a function that takes any number of arguments and 
# returns their sum.
def sumAll(*args):
    result = sum(args)
    print("sum of arguments is: ", result)
    return result

sumAll(1,2,3,4)


# Write a function that prints all keyword arguments passed 
# to it.
def keyWArgs(**kwargs):
    print("Keyword arguments received: ")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

keyWArgs(name="Alice", age=30, country="asia")



# Define a function inside a function and call the inner 
# function.
def outer():
    print("I am outer")

    def inner():
        print("I am inner")
    inner()

outer()


# Demonstrate local and global variable usage in a function.
a = 10
def demo():
    a = 500
    print("Local a: ", a)

demo()
print("Global a: ", a)



# Create a function that accepts another function as an argument.
def greet():
    print("hello")

def executor(function):
    print("Executing passed function")
    function()
executor(greet)

# Another example
a = 20
b = 4
def add(a,b):
    return a + b
def divide(a,b):
    return a/b

def multiplicator(f1, f2, n1, n2):
    added = f1(n1,n2)
    divided = f2(n1,n2)
    print("Added: ", added)
    print("Divided: ", divided)

multiplicator(add, divide, a, b)



# Use a function to apply discount logic on price based on 
# a condition.
def discount(amount):
    if amount > 1000:
        discounted = amount - (amount * 0.1)
    else:
        discounted = amount
    print(f"Price {amount} after discount {discounted}")
    return discounted

discount(5000)


# Write a function that returns another function (closure).
def multiplier(factor):
    def multiply(n):
        return n * factor
    return multiply

times  = multiplier(3)
print(times(5))


# Create a function that counts how many times it’s been
#  called (use attribute).
def countCalls():
    countCalls.counter += 1
    print(f"The counter has been called  {countCalls.counter} times")

countCalls.counter = 0

countCalls()
countCalls()
countCalls()


# Write a function that takes a list of numbers and 
# returns their average.
def average(nums):
    if len(nums) == 0:
        return 0
    else:
        avg = sum(nums) / len(nums)
        print(avg)
        return avg

average([10, 20, 30])

# User input
nums = list(map(int, input("Enter numbers separated by space: ").split()))
average(nums)


#  Create a function with a default parameter and test it 
# with/without a value.
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Alice")   # With value
greet()          # Without value (uses default)
