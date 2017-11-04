import math


class Fugure:
    def get_area(self):
        pass

    def get_perimeter(self):
        pass


class Circle(Fugure):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Fugure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


value = 100
print('Calculating circles and rectangles with basic value ', value)
circle = Circle(value)
rectangle = Rectangle(value, value)
print('Circle area: ', circle.get_area())
print('Circle perimeter: ', circle.get_perimeter())
print('Rectangle area: ', rectangle.get_area())



