# To map with real world scenarios, we started using objects in code

# This is called object oriented programming.

# class and objects

# class is a blueprint for creating objects

# creating class

class Student :
    name = "vishal kumar singh"

# creating object instance
s1 = Student()
print(s1.name)

# Another class

class car :
    color = "Black"
    brand = "Mahindra"

car1 = car()
print(car1.color)
print(car1.brand)

"""
Question : Explain the concept of object-oriented programming (OOP) using Python, focusing on classes and objects.

Answer : Object-oriented programming (OOP) is a programming paradigm that revolves around the concept of classes and objects. In Python, a class serves as a blueprint for creating objects, encapsulating data and behaviors. Objects are instances of classes, possessing attributes and methods that define their characteristics and actions. For example, consider a Student class with attributes like name and age, representing students in a school. Instances of this class, such as student1 and student2, would each have their own values for name and age, allowing for unique identification and manipulation.
"""
