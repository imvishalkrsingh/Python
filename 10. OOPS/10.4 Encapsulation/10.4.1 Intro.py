# Encapsulation:
# Encapsulation is the bundling of data and methods that operate on the data into a single unit, known as an object.
# It involves restricting direct access to some of the object's components and hiding the internal state of an object from the outside world.
# Encapsulation helps in achieving data hiding, abstraction, and modularity, which leads to better code organization and maintenance.

class Car:
    def __init__(self, make, model):
        # Private attributes (data)
        self.__make = make
        self.__model = model
    
    # Public methods (functions) to access and manipulate private attributes
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def set_make(self, make):
        self.__make = make
    
    def set_model(self, model):
        self.__model = model

# Creating an object of the Car class
car1 = Car("Toyota", "Corolla")

# Accessing and manipulating private attributes using public methods
print("Make of car1:", car1.get_make())  # Output: Make of car1: Toyota
print("Model of car1:", car1.get_model())  # Output: Model of car1: Corolla

car1.set_make("Honda")
car1.set_model("Civic")

print("Updated make of car1:", car1.get_make())  # Output: Updated make of car1: Honda
print("Updated model of car1:", car1.get_model())  # Output: Updated model of car1: Civic
