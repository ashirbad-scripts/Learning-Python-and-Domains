# Create a lambda function to square a number.
square = lambda x : x ** 2
print(square(5))


# Create a lambda function that adds 3 numbers.
addThree = lambda a,b,c: a + b + c
print(addThree(4,5,1))


# Use a lambda function inside `map()` to double every 
# number in a list.
numbers = [1,2,3,4,5]
doubled = list(map(lambda x: x**2, numbers))
print(numbers)
print(doubled)


# Use `filter()` with a lambda to extract even numbers 
# from a list.
nums = [10,15,18,21]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

# Use `reduce()` with a lambda to find the product of a list.
from functools import reduce
nums = [1,2,3,4,5]
product = reduce(lambda x,y: x*y, nums)
        # For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) 
        # calculates ((((1+2)+3)+4)+5).
print(product)


# Use a lambda to sort a list of tuples by the second element.
pairs = [(1, 3), (4, 1), (2, 2), (5, 0)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print("Sorted by second element:", sorted_pairs)  # Output: [(5, 0), (4, 1), (2, 2), (1, 3)]


# Create a list of strings and use `map()` to convert them to uppercase.
words = ['apple', 'banana', 'grape']
upperCased = list(map(lambda word: word.upper(), words))
print(upperCased)


# Use `filter()` to find names that start with "A" from a list.
names = ['Alice', 'Bob', 'Andrew', 'Charlie', 'Angela']
filtered = list(filter(lambda eachName: eachName.startswith('A'), names))
print(filtered)


# Create a lambda that returns True if a number is a multiple 
# of both 3 and 5.
check = lambda x: x % 3 == 0 and x % 5 == 0
print(check(9))
print(check(15))


#  Use `map()` with lambda to calculate the length of each 
# string in a list.
fruits = ['apple', 'banana', 'kiwi']
lengths = list(map(lambda eachWord: len(eachWord), fruits))
print(lengths)