# Class to represent a person
class Person:
    def __init__(self, fullName):
        # Initialize instance variables
        self.fullName = fullName

# Create instances of the Person class
person1 = Person("Vishal Kumar Singh")
print("Person 1 full name:", person1.fullName)

# Class to represent a Student
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new student in database")

# Create instances of the Student class
s1 = Student("Aman", 99)
print("Student 1 name:", s1.name)
print("Student 1 marks:", s1.marks)

s2 = Student("Vijay", 98)
print("Student 2 name:", s2.name)
print("Student 2 marks:", s2.marks)

# Types of Constructors: Default Constructor and Parameterized Constructor
# Corrected examples inside the Student class
class Student:
    # Default Constructor
    def __init__(self):
        pass

    # Parameterized Constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new Student in Database")

# Class to represent a laptop
class Laptop:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print("Laptop Started")

# Create objects of the Laptop class
l1 = Laptop("Dell", "Inspiron")
print("Laptop 1 Brand:", l1.brand)
print("Laptop 1 Model:", l1.model)

l2 = Laptop("Apple", "Macbook Air")
print("Laptop 2 Brand:", l2.brand)
print("Laptop 2 Model:", l2.model)

# Static methods - Methods that don't use the self parameter (Work at class level)

class phone:
    @staticmethod  #decorator
    def brand():
        print("Samsung")
    
p1 = phone()
print(p1.brand())

# Decorator allow us to wrap another function in order to extend the behaviour of the wrapped function, without permamently modifying it.
