# Four pillars of OOPs :-
# Abstraction
# Encapsulation
# Inheritance
# Polymorphism

# Abstraction -- Hiding the implementation details of a class and only showing the essentials features to the users.
# Hiding Un-neccessary details

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.ac = True
        self.clutch = True
        print("Car Started")
car1 = Car()
car1.start()