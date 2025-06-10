# Write a simple decorator that prints "Before" and "After" 
# around a function.
def simpleDecorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@simpleDecorator
def sayHello():
    print("hello")
sayHello()

# Arbitary arguments
def simpleDecorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        func(*args, **kwargs)
        print("After")
    return wrapper

@simpleDecorator
def sayHello(name):
    print(f"hello {name}")
sayHello("wills !")



# Create a decorator that measures execution time of a function.
import time
def timeIt(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {start} - {end} sec")
        return result
    return wrapper

@timeIt
def slowFunction():
    time.sleep(1)
    print("Finished Work")

slowFunction()



# Write a decorator that checks if the user is authorized 
# before running a function.
def authorization(func):
    def wrapper(user):
        if user == "admin":
            print("Access granted")
            return func(user)
        else:
            print("Access denied")
    return wrapper

@authorization
def ViewDashboard(user):
    print(f"Welcome to dashboard, {user}")

ViewDashboard("admin")
ViewDashboard("guest")


# Write a decorator that logs the name and arguments of any 
# function it wraps.
def log_args(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments: {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_args
def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

greet("Alice", 30)



# Create a decorator to restrict a function to only run once.
def runOnce(func):
    hasRun = {"called" : False}
    def wrapper(*args, **kwargs):
        if not hasRun["called"]:
            hasRun["called"] = True
            return func(*args, **kwargs)
        else:
            print("Function already exexuted once")
    return wrapper

@runOnce
def initialize():
    print("Initialization")

initialize()
initialize()

# Create a decorator that modifies the return value 
# (e.g., makes it uppercase).
def makeUpperCase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@makeUpperCase
def getMessage(name):
    return f"Hello {name}"

print(getMessage("Willow"))


# Nest two decorators together and observe the execution order.
def decoratorOne(func):
    def wrapper():
        print('Decorator one started')
        func()
        print('Decorator one ended')
    return wrapper

def decoratorTwo(func):
    def wrapper():
        print('Decorator two started')
        func()
        print('Decorator two ended')
    return wrapper

@decoratorOne
@decoratorTwo
def sayHi():
    print("hello Qillwo")
sayHi()

# Create a decorator that repeats a function 3 times.
def repeatThreetimes(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
            print(f"Repeat {i+1}")
            func(*args, **kwargs)
    return wrapper

@repeatThreetimes
def welcome():
    print("Welcome to willowHub")
welcome()


# Build a decorator that catches and logs errors inside the 
# function.
def catchErrors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error occured: ", {e})
    return wrapper

@catchErrors
def divide(a,b):
    return a / b
print(divide(10,2))
print(divide(10,0))


#  Build a decorator that validates function input (e.g., only positive integers allowed).
def validate_input(func):
    def wrapper(n):
        if isinstance(n, int) and n > 0:
            return func(n)
        else:
            print("Invalid input: only positive integers allowed.")
    return wrapper

@validate_input
def square(n):
    return n * n

print("Square of 4:", square(4))
print("Square of -2:", square(-2))
print("Square of 'hello':", square("hello"))
