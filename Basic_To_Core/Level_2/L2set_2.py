# Print numbers 1 to 10 using a for loop.
for i in range(1,10):
    print(i)

# Print even numbers between 1 and 20.
for i in range(2,20,2):
            # start,stop,step
    print(i)

# Print the multiplication table of any number (user input).
num = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{num * i}")

# Calculate the sum of numbers from 1 to 100.
total = 0
for i in range(1, 101):
    print(total + i)

# Print every character in a user-given string.
text = input("Enter a string: ")

for char in text:
    print(char)

# Count how many vowels are in a given string.
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1
print(count)

# Print a pattern like:  
    # *
    # **
    # ***
    # ****
for i in range(1,5):
    print("*" * i)


# Loop through a list of numbers and print only the odd ones.
number = [1,2,3,4,5,6,7,8,9,10]

for num in number:
    if num % 2 != 0:
        print(num)


# Print squares of numbers from 1 to 10.
for i in range(1,11):
    print(i ** 2)

# Take a word and print each character with its position.
word = input("Enter a  word: ")

for i in range(len(word)):
    print(f"Position {i} = {word[i]}")
