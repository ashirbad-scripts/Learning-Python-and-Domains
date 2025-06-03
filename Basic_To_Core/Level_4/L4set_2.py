# Create a tuple with 5 different colors.

# LIST
# colors = ["r", "g", "b"]
# print(colors[1])

# TUPLES
colors = ("red", "blue", "green", "yellow", "purple")
print(colors)
# Access the third item of the tuple.
print(colors[2])
# Try to change the first element of a tuple — observe what happens.
try:
    colors[0] = "black"
except TypeError as e:
    print(e)


# SERIES QUESTIONS -- START
# Create two sets and perform union.
# SETS
set1 = {1,2,3}
set2 = {3,5,6}
unionSet = set1.union(set2)
print(unionSet)

# find their intersection.
insterSect = set1.intersection(set2)
print(insterSect)

# Add a new item to a set.
set2.add(7)
print(set2)


# Remove an item from a set safely (no error if not present).
set1.discard(10)
print("10 is not present: ",set1)
set1.discard(2)
print("2 has been removed : ",set1)
# SERIES QUESTIONS -- END


# Check if a set is a subset of another set.
smallSet = {1,2}
bigSet = {1,4,2,5}
print(smallSet.issubset(bigSet))
print(bigSet.issuperset(smallSet))


# Create a set from a list with duplicate elements.
listWithDuplicates = [1,2,2,3,4,4,5]
uniqueSet = set(listWithDuplicates)
print(uniqueSet)


#  Find the difference between two sets.
s1 = {1,2,3}
s2 = {3,5,6}
diffSet1 = s1.difference(s2)   # diff between set 1 and 2
diffSet2 = s2.difference(s1)   # diff between set 2 and 1

print("These elements present in 1 but not in 2: ",diffSet1)
print("These elements present in 2 but not in 1: ",diffSet2)