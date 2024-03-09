# Create Student class that takes name and marks of 3 subjects as arguments in constructor, then create a method to print the average.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        total_marks = sum(self.marks)
        average_marks = total_marks / len(self.marks)
        print("Hi {}, your average marks: {}".format(self.name, average_marks))

# creating objects
s1 = Student("vishal", [99, 98, 97])
s1.get_avg()

