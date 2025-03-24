# Person class
class Person:
    def __init__(self, name, age, street, zip_city): # constructor
        self.name = name
        self.age = age
        self.street = street
        self.zip_city = zip_city

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        if value is None:
            raise ValueError("Name cannot be empty")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
        if value is None:
            raise ValueError("Age cannot be empty")
        if value <= 0:
            raise ValueError("Age must be greater than zero")
        try:
            value = int(value)
        except:
            raise ValueError("Age must be an integer")

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, value):
        self._street = value
        if value is None:
            raise ValueError("Street cannot be empty")

    @property
    def zip_city(self):
        return self._zip_city

    @zip_city.setter
    def zip_city(self, value):
        self._zip_city = value
        if value is None:
            raise ValueError("Zip/City cannot be empty")

person1 = Person("Ricky", 0.1, "Street 1", "12345 Zip")
print(person1.name, person1.age, person1.street, person1.zip_city)

person2 = Person(None, 0, "Street 2", "67890 Zap")
print(person2.name, person2.age, person2.street, person2.zip_city)



# Shape, Rectangle, Circle classes
class Shape:
    def __init__(self,origin,color,area):
        self.origin = origin
        self.color = color
        self.area = area

    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, value):
        if value is None:
            raise ValueError("Origin cannot be None")
        if not (isinstance(value, (list, tuple)) and len(value) == 2):
            raise ValueError("Origin must be a list or tuple of two numbers")
        self._origin = value
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value):
        if value is None:
            raise ValueError("Color cannot be None")
        self._color = value

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        if value is None:
            raise ValueError("Area cannot be None")     
        self._area = value  

class Circle(Shape):
    def __init__(self, origin, color, area, diameter):
        super().__init__(origin, color, area)
        self.diameter = diameter
        
    @property
    def diameter(self):
        return self._diameter
    
    @diameter.setter
    def diameter(self, value):
        if value <= 0:
            raise ValueError("Diameter cannot be 0 or lower")
        self._diameter = value
        
class Rectangle(Shape):
    def __init__(self, origin, color, area, height, width):
        super().__init__(origin, color, area)
        self.height = height
        self.width = width

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height cannot be 0 or lower")
        self._height = value
        
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width cannot be 0 or lower")
        self._width = value
        
r1 = Rectangle((0,0), "red", 15, 5, 3)
print(r1.origin, r1.color, r1.area, r1.height, r1.width)

c1 = Circle((3,5), "black", 0, 0)
print(c1.origin, c1.color, c1.area, c1.diameter)

#s1 = Shape((0,5),"blue", None)
#print(s1.origin, s1.color, s1.area)