# Create a class `Book` with a constructor that sets title and author.
# Create a method inside `Book` to display "Title by Author."
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Book {self.title} Written by {self.author}")

b1 = Book("Nectar of omniverse", "willow")
print(f"Book 1: {b1.title}, Author: {b1.author}")
b1.display()




# Define a class method (not object method) that prints "Welcome to Bookstore".
class Book:
    @classmethod
    def welcome(cls):
        print("Welcome to bookstore")

Book.welcome()





# Create a class `Student` with a constructor accepting name and marks.
# Write a method to check if a student has passed (marks > 40).
# Create 3 student objects and call the pass/fail method.
class student:

    schoolName = "RiverDale Academy"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def hasPassed(self):
        return self.marks > 33
    
s1 = student("aman", 52)
s2 = student("Tanvi", 31)
s3 = student("Rupa", 89)

# print(s1.name, "Grade Condition: ", s1.hasPassed())
# print(s2.name, "Grade Condition: ", s2.hasPassed())
# print(s3.name, "Grade Condition: ", s3.hasPassed())

# USING LIST (done by me)
studentList = [s1, s2, s3]
for eachStudent in studentList:
    if eachStudent.hasPassed() == True:
        print(f"{eachStudent.name} has passed and scored {eachStudent.marks}")
    else:
        print(f"{eachStudent.name} has failed by scoring {eachStudent.marks}")


# Add a class attribute `school_name` shared by all students.
# Access the `school_name` through an object.
print(f"{s2.name} from {s2.schoolName}")
print(f"{s1.name.capitalize()} belongs to {s1.schoolName}")


#  Change `school_name` at the class level and check if all objects are affected.
# It overwrits that
student.school_name = "Greenhood Academy"

print(s1.school_name)
print(s2.school_name)
print(s3.school_name)





# Create a method that returns a formatted string about the student.
class willow:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def details(self):
        print(f"{self.name} is {self.age} years old")

w1 = willow("Omni", 45)
print(w1.details())










