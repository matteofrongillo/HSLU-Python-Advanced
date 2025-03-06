import matplotlib.pyplot as plt
import math

class Circle:
    def __init__(self, color, xPos, yPos, radius):
        self.color = color
        self.xPos = xPos
        self.yPos = yPos
        self.radius = radius

    def resize(self, size):
        self.radius = self.radius*size
        return "New radius: ", self.radius
    
    def get_origin(self,x,y):
        self.origin = []
        self.origin.append(x + self.xPos)
        self.origin.append(y + self.yPos)
        return self.origin
        
    def set_origin(self,x,y):
        self.origin[0] = x
        self.origin[1] = y
        print(f"New origin: {self.origin}")

    def draw(self):
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
        area = round(3/4*self.radius**2*math.pi,2)
        return area
    