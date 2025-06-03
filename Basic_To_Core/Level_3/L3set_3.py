# Write a function that greets a user with a default name 
# "Guest".
def greet(name = "Johnyia"):
    print(f"Hello {name}")

# johniya is a default name
greet()
# Default name is overwritten
greet("Alice")


# Create a function with a default discount of 10% and 
# calculate final price.
def defaultDiscount(price, discount=10):
    return price - (price * discount/100)
print("By default Discount: ",defaultDiscount(1000))     # --> Default 10%

discountYouWant = int(input("Enter the discount you want: "))
print("New Discount: ",defaultDiscount(1000, discountYouWant))  #-> overwriteen with userinput discount


# Write a function that accepts 3 keyword arguments and 
# prints them.
def display(name="", age=0, city=""):
    print(f"I am {name}, {age} years old from {city}")

display("willow",25,"bbsr")
display(age=25, city="bbsr", name="willow")


# Define a function where default argument is a list, and 
# add items to it.
def addItem(item, itemList=None):
    if itemList is None:
        itemList = []
    itemList.append(item)
    return itemList

print(addItem("apple"))
print(addItem("banana"))


# Create a function with two default parameters and override 
# them in the call.
def introduce(name="John", city="dublin"):
    print(f"Hello, {name}, welcome to {city}")

introduce()
introduce("john")
introduce(name="John", city="BBSR")


# Create a function with mixed required and default parameters.
def mixedReq(name, age=25):
    print(f"my name is {name}, {age} years old")

mixedReq("aman")
mixedReq("aman", 54)


# Write a function that multiplies numbers with optional 
# multiplier (default 2).
def optionalMult(num, multiplier=2):
    return num * multiplier

num = int(input("EAN: "))
print(optionalMult(num))
print(optionalMult(num, 5))

m = int(input("Give a multiplier: "))
print(optionalMult(num, m))


# Call a function using named arguments in a different order.
def diffOrder(name, age=15, city="bbse"):
    return f"{name} is {age} years from {city}"

print(diffOrder("john"))
print(diffOrder(city="amsterdam", name="john"))
print(diffOrder(city="mumbai", age=89, name="alice"))


# Create a function to convert rupees to dollars, with 
# exchange rate as default.
def inrToDollar(ruppees, rate=83.52):
    return ruppees / rate

print(inrToDollar(101))
print(inrToDollar(101, 100))


#  Use None as a default argument and handle it inside the
#  function.
def showMessage(msg=None):
    if msg is None:
        print("No messages")
    else:
        print(f"Message is '{msg}' ")

showMessage()
showMessage("HI there")