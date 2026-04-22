from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
circle = int(input("Enter the radius of the circle: "))
circle = Circle(circle)
rectangle = int(input("Enter the width of the rectangle: ")), int(input("Enter the height of the rectangle: "))
rectangle = Rectangle(*rectangle)
square = int(input("Enter the side of the square: "))
square = Square(square)
print("Area of Circle:", circle.area())
print("Area of Rectangle:", rectangle.area())
print("Area of Square:", square.area())
