import matplotlib.pyplot as plt
import math

class Rectangle:
    def __init__(self, color, xPos, yPos, width, height): #constructor
        self.color = color
        self.xPos = xPos
        self.yPos = yPos
        self.width = width
        self.height = height

    def resize(self, size):
        self.width *= size
        self.height *= size
        return "New width: ", self.width, "New height: ", self.height
    
    def get_origin(self):
        return (self.xPos, self.yPos)

    def set_origin(self, x, y):
        self.xPos = x
        self.yPos = y

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
