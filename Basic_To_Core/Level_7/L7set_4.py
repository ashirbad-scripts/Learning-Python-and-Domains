
# Create a class `Account` with a private attribute `__balance`.
# Create methods `deposit()` and `withdraw()` that update `__balance`.
# Create a method `get_balance()` to safely access `__balance`.
# Try to access `__balance` directly and see what happens.
# Create a setter method to safely change a private attribute.
# Show how private attributes can be *indirectly* accessed using name mangling.
# Create a class with both public and private attributes.
# Create a method that checks if the account is overdrawn (balance < 0).
# Make a transaction log whenever deposit or withdrawal happens.
#  Restrict withdrawal if the amount exceeds the balance.

class Account:
    def __init__(self, name, initialBalance = 0):
        self.name = name
        self.__balance = initialBalance
        self.__transactions = []
    
    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__log_Transactions(f"Deposited: {amount}")
        else:
            print(f"Deposit must be > 0")
    
    # Method to withdraw money
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            self.__log_Transactions(f"withdrawn: {amount}")
    
    # Safely check balance
    def getBalanceInfo(self):
        return self.__balance
    
    # change balance safely
    def changeBalance(self, newBalance):
        if isinstance(newBalance, (int,float)):
            self.__balance = newBalance
        else:
            print("Invalid amount entered")
    
    # To check overdrawn
    def isOverdrawn(self):
        return self.__balance < 0
    
    # Private method to show transcations log
    def __log_Transactions(self, message):
        self.__transactions.append(message)

    # Public method to check transactions history
    def showTransactions(self):
        print(f"Showing transactions for: {self.name}")
        for eachEntry in self.__transactions:
            print(" - ", eachEntry)

    # expose raw via name
    def expose_internal(self):
        print("Accessing Private Balance: ")
        print(self._Account__balance)


# Testing Accounts
acc = Account("Willow", 1000)

print("\n")
# valid operations
acc.deposit(2000)
acc.withdraw(500)
acc.deposit(100)
print(f"Current account balance is {acc.getBalanceInfo()}")


print("\n")
# trying to overdraw
acc.withdraw(5000)


print("\n")
# show transaction log
acc.showTransactions()


print("\n")
# access private attribute directly
try:
    print(acc.__balance)
except AttributeError:
    print("Cannot access private info")


print("\n")
# access private attribute indirectly
acc.expose_internal()


print("\n")
# Maually change the value
acc.changeBalance(10000)
print("New balance is: ", acc.getBalanceInfo())