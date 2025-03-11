import matplotlib.pyplot as plt
import math

class Shape:
    def __init__(self, xPos, yPos, color): #constructor
        self.xPos = xPos
        self.yPos = yPos
        self.color = color

    def get_origin(self):
        return (self.xPos, self.yPos)

    def set_origin(self, x, y):
        self.xPos = x
        self.yPos = y

class Circle(Shape):
    def __init__(self, xPos, yPos, color, radius): #constructor
        super().__init__(xPos, yPos, color)
        self.radius = radius

    def resize(self, size):
        self.radius *= size
        return "New radius: ", self.radius
    
    def draw(self):
        print(f"Circle: color={self.color}, center=({self.xPos}, {self.yPos}), radius={self.radius}")
        fig, ax = plt.subplots()
        circle = plt.Circle((self.xPos, self.yPos), self.radius, color=self.color, fill=False)
        ax.add_patch(circle)
        ax.set_aspect('equal', adjustable='box')
        ax.set_xlim(self.xPos - self.radius - 1, self.xPos + self.radius + 1)
        ax.set_ylim(self.yPos - self.radius - 1, self.yPos + self.radius + 1)
        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')
        ax.plot(self.xPos, self.yPos, 'ro')  # red dot at the center
        
        plt.grid(True)
        plt.show()

    def area(self):
        area = round(self.radius**2*math.pi,2)
        return area
    
class Rectangle(Shape):
    def __init__(self, xPos, yPos, color, width, height): #constructor
        super().__init__(xPos, yPos, color)
        self.width = width
        self.height = height
    
    def resize(self, size):
        self.width *= size
        self.height *= size
        return "New width: ", self.width, "New height: ", self.height
    
    def draw(self):
        print(f"Rectangle: color={self.color}, origin=({self.xPos}, {self.yPos}), width={self.width}, height={self.height}")
        fig, ax = plt.subplots()
        rectangle = plt.Rectangle((self.xPos, self.yPos), self.width, self.height, color=self.color, fill=False)
        ax.add_patch(rectangle)
        ax.set_aspect('equal', adjustable='box')
        ax.set_xlim(self.xPos - 1, self.xPos + self.width + 1)
        ax.set_ylim(self.yPos - 1, self.yPos + self.height + 1)
        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')
        ax.plot(self.xPos, self.yPos, 'ro')  # red dot at the origin
        
        plt.grid(True)
        plt.show()

    def area(self):
        area = round(self.width*self.height,2)
        return area
    
def test_shapes():
    # Test Rectangle
    rect = Rectangle(0, 0, "blue", 10, 5)
    print("Rectangle Area:", rect.area())
    rect.draw()
    rect.resize(2)
    print("Resized Rectangle Area:", rect.area())
    rect.set_origin(5, 5)
    print("Rectangle New Origin:", rect.get_origin())
    rect.draw()

    # Test Circle
    circ = Circle(0, 0, "red", 5)
    print("Circle Area:", circ.area())
    circ.draw()
    circ.resize(2)
    print("Resized Circle Area:", circ.area())
    circ.set_origin(5, 5)
    print("Circle New Origin:", circ.get_origin())
    circ.draw()

test_shapes()