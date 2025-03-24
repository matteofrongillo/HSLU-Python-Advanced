# Properties

class Point:
    def __init__(self, x, y): # constructor
        self._xPos = x
        self._yPos = y

    @property # getter
    def x(self):
        print("Property get x position called\n")
        return self._xPos
    
    @x.setter # setter
    def xPos(self, value):
        if value < 1000:
            self._xPos = value
        else:
            print("Value out of range\n")
    
point = Point(0, 0)
point.xPos += 125

# Magic methods / Dunder methods

# __init__ -> constructor
# __del__ -> destructor
# __str__ -> string representation of an object (output by print())
# __hash__ -> hash value of an object (used in dictionaries)
# __add__ -> allows defining the addition operation (+)
# __len__ -> returns the length of an object (used in len())
# __eq__ -> allows defining the equality operation (==)
# __lt__ -> allows defining the less than operation (<)
# __gt__ -> allows defining the greater than operation (>)

# ------------------------------- EXAMPLES -------------------------------

# __init__ and __str__ example
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    def __str__(self):
        return f"{self._name} is {self._age} years old.\n"
p = Person("Matteo", 22)
print(p) # Output: Matteo is 22 years old.


# __add__ and __eq__ example
class Point:
    def __init__(self, xPos, yPos):
        self._xPos = xPos
        self._yPos = yPos
    def __add__(self, other):
        return Point(self._xPos + other._xPos, self._yPos + other._yPos)
    def __eq__(self, other):
        return self._xPos == other._xPos and self._yPos == other._yPos
    def __str__(self):
        return f"Point({self._xPos}, {self._yPos})"
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3) # Output: Point(4, 6)
print(p1 == p2) # Output: False


# __hash__ example
class Point:
    def __init__(self, xPos, yPos):
        self.__xPos = xPos
        self.__yPos = yPos
    def __eq__(self, other):
        return self.__xPos == other.__xPos and self.__yPos == other.__yPos
    def __hash__(self):
        return hash((self.__xPos, self.__yPos)) # all attributes of Point
    def __str__(self):
        return f"Point({self.__xPos}, {self.__yPos})"
p1 = Point(1, 2)
p2 = Point(1, 2)

if p1 == p2: # comparison with __eq__
    print("p1 and p2 are equal\n")

# ------------------- ValueError and ZeroDivisionError -------------------

try:
    #age = int(input("Age: "))
    age=10
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn’t enter a valid age.")
else:
    print("No exceptions were thrown.\n")

# --- ValueError is "expensive" ---
# If you can avoid raising exceptions, do it

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Invalid Age")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

from timeit import timeit
print("first code ", round(timeit(code1, number=10000)*1000,3), "ms")
print("second code", round(timeit(code2, number=10000)*1000,3), "ms")
print(f"second code is {round((timeit(code1, number=10000)-timeit(code2, number=10000))*1000,3)} ms faster ({round((timeit(code2, number=10000)/timeit(code1, number=10000))*100,1)}% faster)\n")
