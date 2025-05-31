# Take two inputs and perform all arithmetic operations.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponent:", a ** b)
print("Floor Division:", a // b)


# Check if a number is even or odd using modulo operator.
num = int(input("EAN: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Find the square and cube of a number.
num = 5
square = num ** 2
cube = num ** 3

print("Square:", square)
print("Cube:", cube)

# Round a float to 2 decimal places.
float_value = 3.14159
rounded_Floatvalue = round(float_value, 2)
print(rounded_Floatvalue)

#  Convert a string input to integer and add 10.
string_input = input("Enter a string: ")
int_value = int(string_input)
result = int_value + 10
print(result)


# Concatenate two strings with a space in between
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

resultedString = string1 +" "+ string2
print("Concatenated String: ", resultedString)

# Print whether 7 > 5 and 10 == "10" return True or False.
print(7 > 5)
print(10 == "10")

#  Create a variable x = 5 and increase it by 10 using a compound assignment.
x = 5
x += 10
print(x)


# Use input() to ask the user for two numbers and divide the larger by the smaller.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print('Result', a / b)
else:
    print('Result', b / a)

# Create three variables with values 5, 10, 15 and print their average.
a = 5
b = 10
c = 15

average = (a + b + c) / 3
print("Average:", average)
