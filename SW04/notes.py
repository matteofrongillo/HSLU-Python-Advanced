# Superclasses and subclasses

import random

class Point2D:
    def __init__(self, xPos, yPos):
        self._xPos = xPos
        self._yPos = yPos
    def draw(self):
        print(f"2D-Point at ({self._xPos},{self._yPos})")

class Point3D(Point2D):
    def __init__(self, xPos, yPos, zPos=0):
        super().__init__(xPos, yPos)
        self._zPos = zPos

    def draw(self):
        print(f"3D-Point at ({self._xPos},{self._yPos},{self._zPos})")

points = [(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)) for _ in range(1)]

print("Superclasses and subclasses:")
for x, y, z in points:
    p1 = Point2D(x, y)
    p1.draw()
    p2 = Point3D(x, y, z)
    p2.draw()

# Output:
# 2D-Point at (x,y)
# 3D-Point at (x,y,z)

# ----------------------------------

# Static method

class Calculator:

    @staticmethod
    def multiply(a, b):
        return a * b
    
print("\nStatic method 1st example:")
print("Result =", Calculator.multiply(3, 5))

# Output:
# Result = 15

# 2nd example

class Point:
    def __init__(self, xPos, yPos):
        self._xPos = xPos
        self._yPos = yPos
        
    @staticmethod
    def equal(p1, p2):
        return p1._xPos == p2._xPos and p1._yPos == p2._yPos

p1 = Point(3, 4)
p2 = Point(3, 4)

print("\nStatic method 2nd example:")
print("is equal:", Point.equal(p1, p2))    # Call without instance
print("is equal:", p1.equal(p1, p2))       # Call within instance

# Output:
# is equal: True
# is equal: True
