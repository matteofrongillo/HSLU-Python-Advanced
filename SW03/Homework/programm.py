from circle import Circle
from rectangle import Rectangle

def test_shapes():
    # Test Rectangle
    rect = Rectangle("blue", 0, 0, 10, 5)
    print("Rectangle Area:", rect.area())
    rect.draw()
    rect.resize(2)
    print("Resized Rectangle Area:", rect.area())
    rect.set_origin(5, 5)
    print("Rectangle New Origin:", rect.get_origin())
    rect.draw()

    # Test Circle
    circ = Circle("red", 0, 0, 5)
    print("Circle Area:", circ.area())
    circ.draw()
    circ.resize(2)
    print("Resized Circle Area:", circ.area())
    circ.set_origin(5, 5)
    print("Circle New Origin:", circ.get_origin())
    circ.draw()

test_shapes()