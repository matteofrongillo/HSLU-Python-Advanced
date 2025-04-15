# Abstact classes

# An abstract class is a class that cannot be instantiated directly
# It serves as a template for subclasses and defines the basic structure and methods

from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, xPos, yPos):
        self._xPos = xPos
        self._yPos = yPos

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def __init__(self, xPos, yPos, diameter):
        super().__init__(xPos, yPos)
        self._diameter = diameter
c = Circle(1, 2, 3)
c.draw()

# If multiple decorators are used, the @abstractmethod decorator should be placed as far inside as possible

class Shape(ABC):
    def __init__(self, xPos, yPos):
        self._xPos = xPos
        self._yPos = yPos
        
    @property
    @abstractmethod
    def color(self):
        pass