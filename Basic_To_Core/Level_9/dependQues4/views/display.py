from utils.helper import greetUser, isValidName
from models.user import User

def showGreeting():
    name = input("Enter name: ").strip()

    while not isValidName(name):
        print("Please enter a valid name")
        name = input("Enter a valid name: ").strip()
    
    u = User(name)
    g = greetUser(u.getName())
    print(g)