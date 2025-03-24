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
