from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.__salary = salary

    @abstractmethod
    def calculate_salary(self):
        pass

    def get_base_salary(self):
        return self.__salary
    
    def infor(self):
        print(f"Ten: {self.name:<20} - Tuoi: {self.age:<4} - Luong: {self.calculate_salary():<10}")
    
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
    
    def calculate_salary(self):
        return self.get_base_salary()


class Manager(Person):
    def __init__(self, name, age, salary, allowance):
        super().__init__(name, age, salary)
        self.allowance = allowance
        self.__lst_employees = []
    
    def calculate_salary(self):
        return self.get_base_salary() + self.allowance
    
    def get_lst_employees(self):
        return self.__lst_employees
    
    def add_employee(self, employee):
        if employee in self.__lst_employees:
            print(f"Quan li: {self.name} da quan li nhan vien: {employee.name} roi")
        else:
            self.__lst_employees.append(employee)
            print(f"Nhan vien: {employee.name} da duoc quan li boi: {self.name}")
    
    def remove_employee(self, employee):
        if employee not in self.__lst_employees:
            print(f"Nhan vien: {employee.name} khong nam trong danh sach quan li cua: {self.name}")
        else:
            self.__lst_employees.remove(employee)
            print(f"Nhan vien: {employee.name} da bi loai khoi danh sach quan li cua: {self.name}")

def main():
    nv1 = Employee('Quan', 19, 3000000)
    nv2 = Employee('Nhi' , 19, 5000000)
    ql1 = Manager('Trung', 40, 12000000, 700000)
    ql1.add_employee(nv1)
    ql1.add_employee(nv2)

    print(f"Luong cua {nv1.name}: {nv1.calculate_salary()}")
    print(f"Luong cua {nv2.name}: {nv2.calculate_salary()}")
    print(f"Luong cua {ql1.name}: {ql1.calculate_salary()}")

    ql1.remove_employee(nv1)

    ql1.infor()
    nv1.infor()
    nv2.infor()

main()