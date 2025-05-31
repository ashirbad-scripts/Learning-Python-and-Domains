# Take a user's name and greet them using `f-string`.
name = input("EAN: ")
print(f"Hello, {name}!")

# Take three numbers and print the maximum.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

max_value = max(a,b,c)
print(max_value)

# Create a variable that stores the result of `(a + b)^2` using inputs.
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

result = (a + b) ** 2
print("Result of (a + b)^2 is:", result)


# Check the data type after converting `an input` to an int.
value = input("Enter a  number: ")
newValue = int(value)
print(type(newValue))


# Create a program that asks for name, age, and city — then prints a short intro line.
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

print(f"I am {name}, {age} years old from {city}")


# Take a number and print “Positive”, “Negative”, or “Zero”.
num = int(input("Enter a number: "))
if(num > 0):
    print("Positive")
elif (num < 0):
    print("Negative")
else:
    print("ZERO")

# Write code that converts minutes to hours.
minutes = int(input('Enter minutes: '))
hours  = minutes/ 60
print(f"{minutes} mins = {hours} hrs")

# Create a BMI calculator using input for weight and height.
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)
print(f"Your BMI is: {round(bmi, 2)}")


# Take a temperature in Celsius and convert it to Fahrenheit.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")

# Create a program that prints your birth year using your age and current year.
age = int(input("Current age: "))
year = int(input("Current year: "))

birthYear = year - age
print(f"You were born in the year {birthYear}.")