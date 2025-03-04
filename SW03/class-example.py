# Classes, Objects and Instances

class Person:
    def __init__(self, name, age): #constructor
        if len(name) >= 3:
            self.__name = name
        else:
            raise ValueError("Length")
        self.__age = age

    def person_print(self):
        print(f"Name: {self.__name}, Age: {self.__age}")

class Address:
    def __init__(self, zipcode, cityname):
        self.__zipcode = zipcode
        self.__cityname = cityname

    def address_print(self):
        print(f"Zip code: {self.__zipcode}, City: {self.__cityname}")


people = {
    "p1": (Person("Picio Sporcus", 24), Address(9434, "Pisellonia")),
    "p2": (Person("Mister P", 28), Address(434563, "Arraffagemme")),
    "p3": (Person("Anna Foti", 21), Address(6500, "Roma"))
}

for key, (person, address) in people.items():
    print(f"Person {key}:"), {person.person_print(), address.address_print()}
    

# print("p1 is:", p1)
# p2 = Person("Hello")
# p1.foo()

# print("Is p1 an instance of class Person?", isinstance(p1, Person))
# print("Is p1 an instance of class Person?", isinstance(p2, Person))
# print("Is p1 an instance of class Address?", isinstance(p1, Address))

# print("Value of Person object:", p1)
# print("Type of Person object:", type(p1))
# print("Value of Person object:", p2)
# print("Type of Person object:", type(p2))
# print(id(p1), id(p2))