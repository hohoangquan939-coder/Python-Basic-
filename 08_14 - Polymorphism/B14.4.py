from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, age, gender, experience_years):
        self.name = name
        self.age = age
        self.gender = gender
        self.experience_years = experience_years

    @abstractmethod
    def tinh_luong(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, name, age, gender, experience_years, monthly_salary):
        super().__init__(name, age, gender, experience_years)
        self.monthly_salary = monthly_salary

    def tinh_luong(self):
        return round(self.monthly_salary, 2)
    

class PartTimeEmployee(Employee):
    def __init__(self, name, age, gender, experience_years, hours, rate):
        super().__init__(name, age, gender, experience_years)
        self.hours = hours 
        self.rate = rate

    def tinh_luong(self):
        return round(self.hours * self.rate, 2)


class CommissionEmployee(Employee):
    def __init__(self, name, age, gender, experience_years, base_salary, sales, commission_rate):
        super().__init__(name, age, gender, experience_years)
        self.base_salary = base_salary
        self.sales = sales
        self.commission_rate = commission_rate

    def tinh_luong(self):
        return round(self.base_salary + self.sales * self.commission_rate, 2)
    

lst = [
    FullTimeEmployee("Quan", 21, "Nam", 2, 190000),
    FullTimeEmployee("Hung", 21, "Nam", 3, 200000),
    PartTimeEmployee("Minh", 23, "Nam", 3, 120, 35000),
    PartTimeEmployee("Nhi", 21, "Nu", 2, 80, 5000),
    CommissionEmployee("Dung", 32, "Nam", 3, 100000, 300000, 0.1)
]

for i in lst:
    print(f"{i.name} - Luong: {i.tinh_luong()} VND")