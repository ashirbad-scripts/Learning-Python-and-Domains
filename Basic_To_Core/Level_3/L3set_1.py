# Write a function that prints "Hello, World!".
def sayHello():
    print(f"Hello {name}")
name = input("Enter name: ")
sayHello()

# Create a function that takes a name and prints a greeting.
def greet(name):
    print(f"Hello {name}")
greet("Alice")

# Write a function that takes two numbers and returns their sum.
def sum(a,b):
    print(a + b)
sum(5, 3)

# Create a function that returns the square of a number.
def square(num):
    return num ** 2
result = square(5)
print(result)

# ALTERNATE WAY :-
    # def square(num):
    #     return num ** 2
    # print(square(2))



# Write a function that takes a number and returns whether
#  it's even or odd.
def evenOdd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("odd")
evenOdd(4)

# ALTERNATE WAY:-
    # def even_or_odd(num):
    #     if num % 2 == 0:
    #         return "Even"
    #     else:
    #         return "Odd"

    # print(even_or_odd(7))




# Create a function to check if a number is prime.
def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
print(isPrime(11))

# Write a function that returns the maximum of three numbers.
def maxOfThree(a,b,c):
    print(max(a,b,c))
    # return max(a,b,c)

# print(maxOfThree(1,4,5))
maxOfThree(5,8,3)


# Define a function that takes no parameters and returns a 
# random number.
import random
def randomNumber():
    return random.randint(1,10)
print(randomNumber())


# Write a function that converts Celsius to Fahrenheit.
def cToF(celcius):
    return (celcius * 9/5) + 32
print(cToF(25))


#  Call a function multiple times with different inputs 
# and print the outputs.

def multipleTimes(num):
    return num * 2

print(multipleTimes(4))
print(multipleTimes(5))
print(multipleTimes(10))