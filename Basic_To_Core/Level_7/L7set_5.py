# Create a `BankAccount` class where you can deposit, withdraw, and check balance.
class bankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance = amount
            print(f"Deposited: {amount} and New Balance: {self.balance}")
        else:
            print("Invalid amount entered")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}, current balance: {self.balance}")
        else:
            print(f"You dont have that kind of balance, current bal: {self.balance}")

    def checkBalance(self):
        print(f"Current balance: {self.balance}")

# ---- Callings  ----
acc = bankAccount("Aman Gupta")
print(f"Owner Name: {acc.owner}")
print(f"Current balance: {acc.balance}")

acc.deposit(1000)
acc.withdraw(500)
acc.checkBalance()




# Create a `Library` class where books can be issued and returned.
class library:
    def __init__(self, bookList):
        self.books = bookList
        self.issuedBooks = []

    def addBooks(self, b):
        b = input("enter to add: ")
        self.books.append(b)
    
    
    def issueBook(self,book):
        if book in self.books and book not in self.issuedBooks:
            self.issuedBooks.append(book)
            print(f"'{book}' has been issued")
        else:
            print(f"'{book}' is already issued or not registered")
    
    def returnBook(self, book):
        if book in self.issuedBooks:
            self.issuedBooks.remove(book)
            print(f"'{book}' has been returned")
        else:
            print(f"'{book}' was never issued")
    
    def availableBooks(self):
        available = [book for book in self.books if book not in self.issuedBooks]
        print(f"Available Books are: {available}")

# ---- Calling ----
lib = library(["1985", "Python 101", "js mastery"])
lib.availableBooks()

lib.addBooks([])
lib.availableBooks()

lib.issueBook("js mastery")
lib.issueBook("1985")
lib.availableBooks()

lib.returnBook("1985")
lib.returnBook("c coder")
lib.returnBook("js mastery")
lib.availableBooks()




# Create a `Restaurant` class with menu items and order placing.
class restaurant:
    def __init__(self):
        self.menu = {
            "pizza":250,
            "burger":150,
            "fries":100
        }
        self.order = []
    
    def showMenu(self):
        print("Restaurant Menu: ")
        for item, price in self.menu.items():
            print(f"{item} - Rs{price}")
    
    def placeOrder(self, item):
        if item in self.menu:
            self.order.append(item)
            print(f"{item} has been added to order")
    
    def totalBill(self):
        total = sum(self.menu[item] for item in self.order)
        print("Order summary: ", self.order)
        print(f"Total Bill: {total}")

# ---- Calling ----
rest = restaurant()
rest.showMenu()
rest.placeOrder("pizza")
rest.placeOrder("fries")
rest.totalBill()




# Create a `StudentDatabase` class with the ability to add and 
# search students.
class studentsDatabase:
    def __init__(self):
        self.students = {}
    
    def addStudents(self, rollNo, name):
        self.students[rollNo] = name
        print(f"student: {name} bearing rollNo {rollNo} added")
    
    def searchStudent(self, rollNo):
        # return self.students.get(rollNo, "Student not found") #one single way or
        if rollNo in self.students:
            print(f"student found: {self.students[rollNo]}")

# ---- Calling ----
db = studentsDatabase()
db.addStudents(101, "alice")
db.addStudents(150, "john")
# print(db.searchStudent(101))   #if return used
db.searchStudent(150)




# Create a `MovieTicket` class to book and cancel movie tickets.
class movieTicket:
    def __init__(self, availableSeats):
        self.availableSeats = availableSeats
        self.bookedSeats = []
    
    def bookTicket(self, seatNo):
        if seatNo not in self.bookedSeats and seatNo <= self.availableSeats:
            self.bookedSeats.append(seatNo)
            print(f"Seat Number: '{seatNo}' booked")
        else:
            print(f"Seat Numer: '{seatNo}' can not be booked")
    
    def cancelTicket(self, seatNo):
        if seatNo in self.bookedSeats:
            self.bookedSeats.remove(seatNo)
            print(f"seat number: '{seatNo}' cancelled")
        else:
            print(f"seat Number: {seatNo} was never booked")
    
    def showInfo(self):
        print("Current Booked seats: ",self.bookedSeats)

ticket = movieTicket(45)
ticket.bookTicket(3)
ticket.bookTicket(54)
ticket.bookTicket(3)
ticket.bookTicket(20)
ticket.showInfo()
ticket.cancelTicket(20)
ticket.bookTicket(20)
ticket.cancelTicket(8)
ticket.showInfo()






# Create a `ShoppingCart` class where items can be added and removed.
class shoppingCart:
    def __init__(self):
        self.cart = []
    
    def addItems(self, item):
        if item not in self.cart:
            self.cart.append(item)
            print(f"Item: {item} has been added to cart")
        else:
            print("Item is already there")
    
    def removeItems(self, item):
        if item in self.cart:
            self.cart.remove(item)
            print(f"Item: {item} has been removed")
        else:
            print(f"Item is not in cart")
    
    def showCart(self):
        print(f"Items in your cart are: {self.cart}")

cart = shoppingCart()
cart.addItems("Laptop")
cart.addItems("Mobile")
cart.showCart()
print("\n")
cart.removeItems("Mobile")
cart.addItems("headphones")
cart.removeItems("kettle")
cart.showCart()



# Create a `Flight` class with booking, cancellation, and flight details.
class flight:
    def __init__(self, flightNumber, startingPoint, destination, availableSeats=5):
        self.flightNumber = flightNumber
        self.startingPoint = startingPoint
        self.destination = destination
        self.availableSeats = availableSeats
        self.bookedSeats = 0
    
    def bookTicket(self):
        if self.availableSeats > 0:
            self.availableSeats -= 1
            self.bookedSeats += 1
            print(f"Ticket booked!!, Seats available: {self.availableSeats}")
        else:
            print(f"No seats available")
    
    def cancelTicket(self):
        if self.bookedSeats > 0:
            self.availableSeats += 1
            self.bookedSeats -= 1
            print(f"Ticket cancelled, Seats available: {self.availableSeats}")
        else:
            print("No bookings to cancel")
    
    def flightDetails(self):
        print("Flight Details: ")
        print(f"Flight number: {self.flightNumber}")
        print(f"Flight Origin: {self.startingPoint}")
        print(f"Flight Destination: {self.destination}")
        print(f"Available Seats: {self.availableSeats}")
        print(f"Booked seats: {self.bookedSeats}")

f = flight('a103rt', "India", "Dubai")
f.flightDetails()
print("\n")
f.bookTicket()
f.bookTicket()
f.cancelTicket()
print("\n")
f.flightDetails()



# Create a `School` class with multiple students and teachers.
class school:
    def __init__(self, schoolName):
        self.schoolName = schoolName
        self.students = []
        self.teachers = []
    
    def addStudents(self, S_name):
        self.students.append(S_name)
        print(f"'{S_name}' was registered in {self.schoolName}")
    
    def addTeachers(self, T_name):
        self.teachers.append(T_name)
        print(f"{T_name} became teacher at {self.schoolName}")
    
    def showMembers(self):
        print(f"Welcome to {self.schoolName}")
        # simple way
        # print(f"Teachers are: {self.teachers}")
        # print(f"Students are: {self.students}")

        # Complex way
        print("Students:- ")
        for eachStudent in self.students:
            print(f" -> {eachStudent}")

        print("Teachers:- ")
        for eachTeacher in self.teachers:
            print(f" -> {eachTeacher}")

s = school("Riverdale Academy")
s.addStudents("John")
s.addStudents("Alice")
s.addStudents("Morgan")
s.addTeachers("Mr. moriarty")
s.addTeachers("Mr. Psycho")
s.showMembers()



# Create a `QuizGame` class that manages a set of questions and answers.
class quizGame:
    def __init__(self):
        self.questions = {
            'Capital of India' : 'delhi',
            'language in ai' : 'python'
        }
    
    def askQuestions(self):
        score  = 0
        for q, a in self.questions.items():
            ans = input(q + " ")
            if ans.strip().lower() == a.lower():
                print("Correct")
                score += 1
            else:
                print("wrong")
            print(f"Final Score is : {score} / {len(self.questions)}")

q = quizGame()
q.askQuestions()



#  Create a `TaskManager` class to create, update, and delete tasks.
class TaskManager:
    def __init__(self):
        self.tasks = {}

    def addTask(self, taskID, desc):
        if taskID in self.tasks:
            print(f"Task ID {taskID} already exists.")
        else:
            self.tasks[taskID] = desc
            print(f"'{desc}' was added.")

    def updateTasks(self, taskID, newDesc):
        if taskID in self.tasks:
            self.tasks[taskID] = newDesc
            print("Task updated.")
        else:
            print("Task not found.")

    def deleteTask(self, taskID):
        if taskID in self.tasks:
            desc = self.tasks.pop(taskID)
            print(f"'{desc}' was deleted.")
        else:
            print("Task not found.")

    def showTasks(self):
        if not self.tasks:
            print("No tasks available.")
        for id, desc in self.tasks.items():
            print(f"{id}: {desc}")


# Example usage
tm = TaskManager()
tm.addTask(1, "Buy grocery")
tm.addTask(2, "Practice JS")
tm.showTasks()
print("\n")

tm.updateTasks(1, "Watch movie")
tm.showTasks()
print("\n")

tm.deleteTask(2)
tm.showTasks()
