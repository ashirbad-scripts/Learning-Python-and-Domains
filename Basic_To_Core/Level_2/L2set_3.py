# Use a while loop to print numbers 1 to 5.
i = 1
while i <= 5:
    print(i)
    i += 1

# Print numbers in reverse from 10 to 1 using while.
i = 10
while i >= 1:
    print(i)
    i -= 1

# Take input until the user enters "exit".
while True:
    user_Input = input("Type exit to quit: ")
    if user_Input.lower() == "exit" or user_Input.lower() == "quit":
        break

# Use a loop to guess a number (loop ends when guessed correctly).
secret = 7
while True:
    guess = int(input("Guess the number: "))
    if guess == secret:
        print("Correct")
        break
    else:
        print("try Again")


# Print the factorial of a number using a while loop.
num = int(input("Enter a number: "))
result = 1
i = 1

while i <= num:
    result *= i
    i += 1

print("Factorial is:", result)


# Print the first 10 Fibonacci numbers.
a,b = 0,1
count = 0

while count < 10:
    print(a)
    a,b = b, a+b 
    count += 1


#  Take input for a number, keep asking until a positive number 
# is entered.

while True:
    number = int(input("Enter a negative number to quit : "))
    if number < 0:
        print("Congrats")
        break;


# Use a loop with break to stop at the first number divisible 
# by 7 from 1–100.

i = 1
while i <= 100:
    if i % 7 == 0:
        print("First number divisible by 7 is ", i)
        break
    i += 1


# Loop through numbers 1 to 20, but continue if the number 
# is divisible by 3.

i = 1
while i <= 20:
    if i % 3 == 0:
        i += 1
        continue

    print(i)
    i += 1


# Use a loop to find the sum of digits of a number.
num = int(input("Enter a number: "))
total = 0

while num > 0:
    digit = num % 10
    total += digit
    num = num // 10
print(total)