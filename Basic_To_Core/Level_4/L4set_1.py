# SERIES QUESTIONS
# Create a list of 5 fruits and print it.
fruits = ["apple", "banana", "mango", "orange", "grape"]
print(fruits)

# Add a new fruit to the end of the list.
fruits.append("pineapple")
print("appended pineapple:  ",fruits)

# Insert a fruit at the second position.
fruits.insert(1, "kiwi")
print("Inserted kiwi: ",fruits)

# Remove a fruit by name.
fruits.remove("banana")
print("Removed banana: ",fruits)

# Remove the last item using a method.
fruits.pop()
print("Removed last fruit: ",fruits)

# Print the first and last element of the list.
print("First fruit is : ",fruits[0])
print("Second fruit is : ",fruits[-1])

# Sort the list alphabetically.
fruits.sort()
print("Sorted fruits: ",fruits)
# SERIES QUESTIONS -- END


# Create a list of numbers and find the maximum number.
numbers = [12, 45, 7, 22, 89]
print(max(numbers))

# Reverse a list without using reverse method.
givenList = input("Enter elements separated by space: ").split()
reverse_list = givenList[::-1]
print(reverse_list)

# for numbers in list:-
givenList_str = input("Enter numbers separated by comma: ").split(',')
givenList_int = [int(eachItem) for eachItem in givenList_str]
reverse_list = givenList_int[::-1]
print(reverse_list)


#  Take 5 user inputs and store them into a list.
user_input = []

for _ in range(5):
    uI = input("Enter an item: ")
    user_input.append(uI)
print(user_input)
