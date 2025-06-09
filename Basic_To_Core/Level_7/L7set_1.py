# Create a class named `Car` with attributes `brand` and `model`.
class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def run(self):
        print(f"{self.brand} {self.model} is running")

# Create an object of the `Car` class and print its attributes.
car1 = car("Toyota", "Innova")
print(f"Car 1 brand {car1.brand} and model is {car1.model}")

# Define a method inside `Car` that prints "Car is running".
car1.run()

# Create another object of the same class with different values.
car2 = car("Honda", "civic")
print(f"Car 2 brand {car2.brand} and model is {car2.model}")
car2.run()


# Create a class `Person` with attributes `name` and `age`.
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def anything_display(self):
        print(f"Name: {self.name}, Age:{self.age}")


# Instantiate a `Person` object and display its information.
person1 = person("John", 22)
person1.anything_display()







# Create a method `is_adult()` inside `Person` class 
# (returns True if age > 18).
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def isAdult(self):
        return self.age > 18
    
    def anything_display(self):
        print(f"Name: {self.name}, Age:{self.age}")

person2 = person("Johuyn", 22)
print("Is Adult ? ", person2.isAdult())

# Modify the `age` attribute of a `Person` object after creation.
person2.age = 30
print("Updated age: ", person2.age)




# Add a method that changes the `name` attribute.
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def modifyingAttribute(self, new_name):
        self.name = new_name
    
    def anything_display(self):
        print(f"Name: {self.name}, Age:{self.age}")

person3 = person("Alice", 22)
print("Current name: ", person3.name)

person3.modifyingAttribute("ayankoji")
print("Updated name : ", person3.name)

person3.anything_display()





#  Create multiple objects of the `Person` class and store 
# them in a list.
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def isAdult(self):
        return self.age > 18
    
    def run(self):
        print(f"Name: {self.name}, Age: {self.age}")

# storing multiple objects of person class in peopleList
person1 = person("John", 17)
person2 = person("Lily", 21)
person3 = person("Raj", 15)
person4 = person("Zara", 19)

peopleList = [person1, person2, person3, person4]

# Looping through and displaying info
for eachPerson in peopleList:
    eachPerson.run()
    person2.run()

    print("Is adult ? ", person2.isAdult())
    print("Is adult ? ", person1.isAdult())
    print("Is adult ? ", eachPerson.isAdult())