import random
fruits = ["apple", "orange", "peach", "cranberry"]
picked1 = random.choices(fruits, k=2)
picked2 = random.choices(fruits, k=10)

print(picked1)
print(picked2)
