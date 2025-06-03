# Create a dictionary with three key-value pairs (name, age, city).
person = {"name":"alice", "age":25}
print(person)

# Add a new key-value pair to the dictionary.
person["profession"] = "Teacher"
print(person)

# Update the value of an existing key.
person["age"] = 52.
print(person)

# Delete a key-value pair.
del person["profession"]
print(person)

# Access a value using its key.
print(person["name"])

# Use a loop to print all keys.
for eachKey in person.keys():
    print(eachKey)

# Use a loop to print all key-value pairs.
for eachKey, eachValue in person.items():
    print(f"{eachKey} : {eachValue}")

# Check if a key exists in the dictionary.
print("age" in person)
# SERIES QUESTIONS -- END


# Create a dictionary where keys are numbers and values are their 
# squares.
sqaures = {num: num ** 2 for num in range(1,6)}
print(sqaures)

#  Merge two dictionaries into one.
dict1 = {"a":1, "b":2}
dict2 = {"c":2, "d":3}
merged = {**dict1 ,**dict2}
print(merged)