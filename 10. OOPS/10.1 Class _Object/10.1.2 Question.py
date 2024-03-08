class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Creating instances of Rectangle class
rectangle1 = Rectangle(5, 4)
rectangle2 = Rectangle(7, 3)

# Printing details of rectangle1
print("Rectangle 1:")
print("Length:", rectangle1.length)
print("Width:", rectangle1.width)
print("Area:", rectangle1.area())
print("Perimeter:", rectangle1.perimeter())

# Printing details of rectangle2
print("\nRectangle 2:")
print("Length:", rectangle2.length)
print("Width:", rectangle2.width)
print("Area:", rectangle2.area())
print("Perimeter:", rectangle2.perimeter())
