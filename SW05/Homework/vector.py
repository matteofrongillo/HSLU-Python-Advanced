class Vector:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __mul__(self, other):
        return Vector(self._x * other._x, self._y * other._x)
    
    def __str__(self):
        return f"Vector({self._x}, {self._y})"
        
v1 = Vector(1,6)
v2 = Vector(4,1)
v3 = v1*v2
print(v3)