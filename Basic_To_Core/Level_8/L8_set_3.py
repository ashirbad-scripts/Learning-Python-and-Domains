# Write a recursive function to calculate factorial.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print("Factorial of 5: ", factorial(5))


# Write a recursive function to calculate Fibonacci numbers.
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n -1 ) + fibonacci(n - 2)
print("Fibonacci number at position 8 is: ", fibonacci(8))


# Write a recursive function to sum all numbers from 1 to n.
def sumTon(n):
    if n == 0:
        return 0
    else:
        return n + sumTon(n-1)

print("Sum of all number from 1 to 5 are: ", sumTon(5))


# Write a recursive function to reverse a string.
def reverseString(text):
    if len(text) == 0:
        return text
    else:
        return reverseString(text[1:]) + text[0]

print("Reverse of hello is: ", reverseString("hello"))


# Write a recursive function to find the GCD of two numbers.
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print("GCD of 48 and 18 are: ", gcd(48,18))


# Create a recursive function to calculate the power of a number.
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp-1)
    
print("2 ^ 4 is: ", power(2,4))
# LOGIC
#             power(2, 4)
#             = 2 * power(2, 3)
#             = 2 * (2 * power(2, 2))
#             = 2 * (2 * (2 * power(2, 1)))
#             = 2 * (2 * (2 * (2 * power(2, 0))))
#             = 2 * (2 * (2 * (2 * 1)))         # base case: power(2, 0) = 1




# Write a recursive function to find the max element in a list.
def findMax(list):
    if len(list) == 1:
        return list[0]
    maxOfRest = findMax(list[1:])
    return list[0] if list[0] > maxOfRest else maxOfRest

print("Max in [1, 9, 3, 7]:", findMax([1, 9, 3, 7]))


# Write a recursive function to flatten a nested list.
def flatten(lis):
    flat = []
    for item in lis:
        if isinstance(item, list):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat

nested = [1, [2, [3, 4]], 5]
print("Flattened list:", flatten(nested))


# Use recursion to count the number of digits in a number.
def countDigits(n):
    if n < 10:
        return 1
    else:
        return 1 + countDigits(n // 10)

print("Number of digits in 12345 is: ", countDigits(12345))


# Use recursion to check if a string is a palindrome.
def ispalindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return ispalindrome(s[1:-1])

print("Is 'madam' a palindrome?", ispalindrome("madam"))