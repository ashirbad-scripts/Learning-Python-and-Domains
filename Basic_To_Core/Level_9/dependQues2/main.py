import tools as t

print("Default name: ", t.greet())
print("Custom name: ", t.greet("John"))

print(t.add(2,3))

x = int(input("Enter a num 1: "))
y = int(input("Enter a num 2: "))
print(f"Sum of {x} and {y} is {t.add(x,y)}")
