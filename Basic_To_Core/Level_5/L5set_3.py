# Use `.format()` to insert two numbers into a sentence.
print("Inserted numbers are {} and {}".format(5, 10))

# Format a floating-point number to two decimal places.
num = 3.1415
print("{:.2f}".format(num))

# Use f-strings to print a name and age.
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")


# Use f-strings to perform math inside a string (like `5 + 7`).
print(f"Sum of 5 and 10 is {5 + 10}")

# Create a formatted string showing product name, quantity, 
# and price.
pName = "Laptop"
Pqty = 20
pprice = 75000
print(f"{pName} is Rs.{pprice} and stock available is {Pqty}")

# Pad a number with leading zeros (e.g., 5 becomes `0005`).
num = 5
print(f"{num:04}")

# Create a multi-line f-string that includes variables.
name = "Bob"
city = "New York"
print(f"""
Hello my name is {name} 
and 
I live in {city}
""")


# Use `.format()` method with named placeholders.
print("Name : {n}, age: {a}".format(n="john", a=28))
print("Book: {b}, quantity: {q}".format(b="Nectar of mountain", q=200))


# Align text to left, center, and right using formatting.
word = "willaw"
print("{:<10}".format(word))
print("{:^10}".format(word))
print("{:>10}".format(word))

# Pattern to look better
print("{:^10}".format(word))
print("{:<10}".format(word))


#  Insert a variable into a string inside a loop using f-strings.
for i in range(1, 5):
    print(f"{i} has been processed")