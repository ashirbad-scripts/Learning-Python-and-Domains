# Create a class `Animal` with a method `make_sound()`.
class animal:
    def makeSound(self):
        print(f"Making sounds")

    # Create a method in `Animal` that prints "Eating food".
    def eat(self):
        print("Eating food")


# Create a class `Dog` that inherits from `Animal`.
# Override `make_sound()` in `Dog` to print "Bark!".
class Dog(animal):
    def makeSound(self):
        print("Bark")


# Create another subclass `Cat` that overrides `make_sound()`.
class Cat(animal):
    def makeSound(self):
        print("Meow!!")

# Access a parent class method from a child class object.
generic_animal = animal()
dog = Dog()
cat = Cat()

print("== animal ==")
generic_animal.makeSound()   # Should print generic sound
generic_animal.eat()  

print("== DOG ==")
dog.makeSound()
dog.eat()

print("== CAT ==")
cat.makeSound()
cat.eat()




# Create a base class Vehicle
class vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels
    
    def showInfo(self):
        print(f"Brand: {self.brand}, Wheels: {self.wheels}")
    
    def startEngine(self):
        print("Engine Started")


# Create subclasses Bike and Truck
class bike(vehicle):
    def __init__(self, brand):
        super().__init__(brand, wheels=2)

    def startEngine(self):
        print("Bike engine started")

class truck(vehicle):
    def __init__(self, brand):
        super().__init__(brand, wheels=12)
    
    def cargoLoad(self):
        print("Cargo Loaded")
    
    def startEngine(self):
        print("Truck Engine started")

print("== Vehicle ==")
v = vehicle("Generic", 4)
v.showInfo()
v.startEngine

print("== Bike ==")
b = bike("Yamha")
b.showInfo()
b.startEngine

print("== Truck ==")
t = truck("volvo")
t.showInfo()
t.cargoLoad()
t.startEngine()