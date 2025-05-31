# Take an age input and print whether the person is a minor, 
# adult, or senior.

age = int(input("EYA :"))
if(age < 18):
    print("Minor")
elif age > 18 and age < 60:
    print("Adult")
else:
    print("Senior")

# Check whether a number is positive, negative, or zero.
num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# Take two numbers and print the larger one.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Larger number is:", a)
elif b > a:
    print("Larger number is:", b)
else:
    print("Both numbers are equal.")


# Take a number and print whether it is divisible by 3 and 5.
number  = int(input("Enter a number: "))
if number % 5 == 0 and number % 3 == 0:
    print("It is divisible by both 5 and 3")
else:
    print("Not divisible")

# Check if a year is a leap year.
year = int(input("Enter a year: "))

if year % 4 == 0:
    print("It is a leap year")
else:
    print("Not a leap year")

# Ask the user for a username and password — print “Access Granted” only if both are correct.
username = input("Enter username: ")
password = input("Enter password: ")

if username == password:
    print("Access Granted")
else:
    print("Out")

# Take three numbers and print the greatest one.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print(f"{a} is the greatest among {a},{b},{c}")
elif b >= c and b >= a:
    print(f"{b} is the greatest among {a},{b},{c}")
else:
    print(f"{c} is the greatest among {a},{b},{c}")

# Ask for marks and print grade: A (90+), B (75–89), C (50–74), F (<50).
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")


# Check if a number is within a range (10–50).
num = int(input("EAN: "))

if num >= 10 and num <= 50:
    print("In Range")
else:
    print("Not in range")

#Take input for gender and age, and print eligibility for a specific 
# program (custom rule).
gender = input("Enter gender (M/F): ")
age = int(input("Enter age: "))

if gender.upper() == 'M' and (age >= 20 and age <= 50):
    print("Entry allowed")
else:
    print("Entry Denied")

