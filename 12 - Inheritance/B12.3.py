class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def gioi_thieu(self):
        print(f"Toi ten la {self.name}, {self.age} tuoi")


class Employee(Person):
    tax_rate = 0.1
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def tinh_thue(self):
        return round(self.salary * self.tax_rate,3)
    
    def gioi_thieu(self):
        super().gioi_thieu()
        print(f"Luong: {self.salary} - Thue: {self.tinh_thue()}")


class Manager(Employee):
    tax_rate = 0.15
    def __init__(self, name, age, salary, team_size):
        super().__init__(name, age, salary)
        self.team_size = team_size

    def tinh_thue(self):
        return round(self.salary * self.tax_rate, 2)
    
    def gioi_thieu(self):
        super().gioi_thieu()
        print(f"So nhan vien quan li: {self.team_size}")
           
    
p = Person("An", 25)
e = Employee("Binh", 30, 15000000)
m = Manager("Chi", 35, 25000000, 5)

p.gioi_thieu()
e.gioi_thieu()
m.gioi_thieu()