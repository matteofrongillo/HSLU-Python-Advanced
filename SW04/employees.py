from random import choices

class Employee:
    _num_employees = 0

    def __init__(self, name):
        self.name = name
        Employee._num_employees += 1
        self._employees_no = Employee._num_employees

    def print(self):
        print(f"Employee[name='{self.name}'], no='[{self._employees_no}]'")

lst = []
for i in choices("ABCDEFGHIJKLMNOPKRSTUVWXYZ", k=10):
    lst.append(Employee(str(i)))
    # print("_num_employees:", Employee._num_employees)

for elem in lst:
    elem.print()