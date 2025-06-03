# Write a function to calculate the area of a rectangle.
def callReactangle(l,b):
    return l * b

x = int(input("Enter the length: "))
y = int(input("Enter breadth: ")) 
print(callReactangle(x,y))

# print(callReactangle(4,5))  --> Hard-coded values!!

# Create a function that calculates the factorial of a number.
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i


# Write a function that takes a list and returns the sum 
# of its elements.
def listSum(numbers):
    total = 0
    for num in numbers:
        total = total + num
    print(total)
    # return total

# print(listSum([1,5,4]))  --> If we reurn instead of printing
listSum([2,5,4,3])


# Write a function that takes a number and returns a list 
# of its divisors.
def findDivisors(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

print(findDivisors(12))
            # LOGIC :- If n is divided by i (that is each number)
            #           then append the i that divided n and left 0
            #           as remainder



# Create a function that checks if a string is a palindrome.
def isPalindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]

print(isPalindrome("Madam"))
print(isPalindrome("A man a plan a canal Panama"))


# Write a function that counts the number of vowels in a string.
def vowelCount(text):
    vowels = "aeiouAEIOU"
    count = 0
    for eachWord in text:
        if eachWord in vowels:
            count += 1
    return count

print(vowelCount("Willow"))

# Create a function that finds the greatest common divisor (GCD) of two numbers.



# Write a function to return the average of a list of numbers.
# print(sum([1,2,3])) -- logic for sum of list elements

def averageOfList(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)
print(averageOfList([5,1,4,2]))

# Create a function that capitalizes the first letter of each word in a sentence.
def capitalizeLetters(sentence):
    words = sentence.split()
    capitalized_words = []

    for eachWord in words:
        capitalized_words.append(eachWord.capitalize())
    return " ".join(capitalized_words)
print(capitalizeLetters("hello  i am from python"))


#  Write a function to reverse a string without using slicing.
def reverseString(text):
    reversed_text = ""
    for eachChar in text:
        reversed_text = eachChar + reversed_text
    return reversed_text
print(reverseString("pyhton"))
