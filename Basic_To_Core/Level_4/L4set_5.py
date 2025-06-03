# List to Dict Pairing
def listToDict(keys, value):
    result = {}
    for i in range(len(keys)):
        result[keys[i]] = value[i]
    return result

keys = ["id", "name", "age"]
value = [1, "Alice", 30]
print(listToDict(keys, value))


# Remove the duplicates the given list without creating a new list.
def removeDup(lst):
    seen = set()
    i = 0
    while i < len(lst):
        if lst[i] in seen:
            lst.pop()
        else:
            seen.add(lst[i])
            i += 1

sample_list = [1, 2, 2, 3, 1]
removeDup(sample_list)
print(sample_list)


# Count how many times each character appears.
def countChar(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    return count
print(countChar("Apple"))



# Group words by starting letter.
def groupByFirst(words):
    result = {}
    for eachWord in words:
        first = eachWord[0]
        if first not in result:
            result[first] = []
        result[first].append(eachWord)
    return result

print(groupByFirst(["apple", "art", "ball", "bat"]))


# Find the key with the maximum value.
def macValueKey(d):
    return max(d, key=d.get)

print(macValueKey(({'a': 5, 'b': 9, 'c': 3})))


# Find common elements between two lists.
def commonE(list1, list2):
    return set(list1) & set(list2)
print(commonE([1, 2, 3, 4], [3, 4, 5, 6]))


# Symmetric difference
def symmetricDiff(set1,set2):
    return set1 ^ set2
print(symmetricDiff({1,2,3}, {3,4,5}))