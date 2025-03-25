# Enums are special data type for defining symbolic names for a fixed set of constant values

from enum import Enum, IntEnum, StrEnum # or from strenum import StrEnum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED)
print(Color.RED.name)
print(Color.RED.value)

for color in Color:
    print(color)

class Status(IntEnum):
    OK = 200
    NOT_FOUND = 404
    SERVER_ERROR = 500

print(Status.OK)

class Color2(StrEnum):
    RED = "red"

print(Color2.RED)

# Polymorphism

class MyBaseClass:
    def output(felf):
        raise NotImplementedError()
class MyClassA(MyBaseClass):
    def output(self):
        print("A profile has been chosen")
class MyClassB(MyBaseClass):
    def output(self):
        print("B profile has been chosen")

obj = None

while True:
    choice = input("Use class A or B? ")

    if choice.upper() == "A":
        obj = MyClassA()
        break

    elif choice.upper() == "B":
        obj = MyClassB()
        break

    else:
        print("Profile not valid")
        continue

obj.output()