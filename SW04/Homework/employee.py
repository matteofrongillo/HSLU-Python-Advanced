class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Name: {self.name}, Salary: {str(self.salary)}"
    
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_details(self):
        return f"Name: {self.name}, Salary: {str(self.salary)}, Department: {self.department}"
    
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def get_details(self):
        return f"Name: {self.name}, Salary: {str(self.salary)}, Programming Language: {self.programming_language}"
    
dev = Developer("Paul Allen", 70000, "Assembler")
mgr = Manager("Bill Gates", 90000, "IT")
print(dev.get_details()) # Output: Name: Paul Allen, Salary: 70000, Programming Language: Assembler
print(mgr.get_details()) # Output: Name: Bill Gates, Salary: 90000, Department: IT