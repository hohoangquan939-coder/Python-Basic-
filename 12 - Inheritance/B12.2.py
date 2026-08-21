class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def thong_tin(self):
        print(f"Ten: {self.name} - Luong: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def thong_tin(self):
        print(f"Ten: {self.name} - Luong: {self.salary} - Bonus: {self.bonus}")


Em = Employee("Quan", 19)
Ma = Manager("Huy", 30, 5)

Em.thong_tin()
Ma.thong_tin()