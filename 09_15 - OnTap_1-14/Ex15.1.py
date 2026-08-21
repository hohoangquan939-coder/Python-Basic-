# Bài hệ thống 1 — Quản lý Sở thú (Zoo Management)
from abc import ABC, abstractmethod
# ABC: Abstract base class
class Animal(ABC):
    def __init__(self, name, age, food_amount):
        self.name = name
        self.age = age
        self.__food_amount = food_amount  #Private
    
    @abstractmethod
    def phat_am_thanh(self): 
        pass
        
    @abstractmethod
    def loai_thuc_an(self): 
        pass

    def get_food_amount(self):
        return self.__food_amount
    
    def set_food_amount(self, food_amount):
        if food_amount < 0: print(f"Loi: Luong thuc an khong the be hon 0")
        else:
            self.__food_amount = food_amount

    def thong_tin(self):
        print(f"Ten: {self.name} - Tuoi: {self.age} - An: {self.__food_amount} (kg) moi ngay")        

# Class Lion
class Lion(Animal):
    def __init__(self, name, age, food_amount, pride_size):
        super().__init__(name, age, food_amount)
        self.pride_size = pride_size

    def phat_am_thanh(self):
        print(f"{self.name} Roarrrrrrrr")
    
    def loai_thuc_an(self):
        return "Thit"
    
# Class Elephant
class Elephant(Animal):
    def __init__(self, name, age, food_amount, trunk_length):
        super().__init__(name, age, food_amount)
        self.trunk_length = trunk_length

    def phat_am_thanh(self):
        print(f"{self.name} Trumpetttttttttt")
    
    def loai_thuc_an(self):
        return "Thuc vat"

# Class Monkey
class Monkey(Animal):
    def __init__(self, name, age, food_amount):
        super().__init__(name, age, food_amount)

    def phat_am_thanh(self):
        print(f"{self.name} Whopppppppppppp")
    
    def loai_thuc_an(self):
        return "Thuc vat"
    
    def leo_cay(self):
        print(f"{self.name} dag leo cay")

#Class Zoo
class Zoo:
    def __init__(self, name):
        self.name = name
        self.__animals = []

    def get_animals(self):
        return self.__animals

    def them_dong_vat(self, animal):
        self.__animals.append(animal)

    def tong_thuc_an_can_thiet(self):
        total = 0
        for i in self.__animals:
            total += i.get_food_amount()
        return total

    def danh_sach_theo_loai_thuc_an(self, loai):
        lst = []
        for i in self.__animals:
            if i.loai_thuc_an() == loai: 
                lst.append(i.name)
        return lst

    def tat_ca_keu(self):
        for i in self.__animals:
            i.phat_am_thanh()

    def luu_file(self, filename):
        with open(filename, 'w') as f:
            for i in self.__animals:
                f.write(f"Ten: {i.name} - Tuoi: {i.age} - Loai thuc an: {i.loai_thuc_an()} - Luong thuc an: {i.get_food_amount()}\n")

    def doc_file(self, filename):
        try: 
            with open(filename, 'r') as f:
                for line in f:
                    print(line)

        except FileNotFoundError:
            print(f"Loi! Khong tim thay file")

def kiem_tra_nhap_so(x):
    try:
        float(x)
        return True
    except ValueError: 
        return False

def nhap_so_thuc():
    so = input()
    while not kiem_tra_nhap_so(so):
        so = input("Loi! Phai nhap so: ")
    return float(so)

def main():
    zoo_name = input("Nhap ten so thu: ")
    system_zoo = Zoo(zoo_name)
    
    while True:
        animal_name = input("Chon loai (lion/elephant/monkey/end): ")

        if animal_name == 'end':
            break

        elif animal_name == 'lion':
            lion_name = input("Nhap ten: ")
            print(f"Nhap tuoi: ", end = "")
            lion_age = nhap_so_thuc()
            print(f"Nhap luong thuc an (kg/ngay): ", end = "") 
            lion_food_amount = nhap_so_thuc()
            print(f"Nhap so luong bay dan: ", end = "")
            lion_pride_size = nhap_so_thuc()

            sv_lion = Lion(lion_name, lion_age, lion_food_amount, lion_pride_size)
            system_zoo.them_dong_vat(sv_lion)

        elif animal_name == 'elephant':
            elephant_name = input("Nhap ten: ")
            print("Nhap tuoi: ", end = "")
            elephant_age = nhap_so_thuc()
            print(f"Nhap luong thuc an (kg/ngay): ", end = "")
            elephant_food_amount = nhap_so_thuc()
            print("Nhap chieu dai voi (m): ", end = "")
            elephant_trunk_length = nhap_so_thuc()

            sv_elephant = Elephant(elephant_name, elephant_age, elephant_food_amount, elephant_trunk_length)
            system_zoo.them_dong_vat(sv_elephant)

        elif animal_name == 'monkey':
            monkey_name = input("Nhap ten: ")
            print("Nhap tuoi: ", end="")
            monkey_age = nhap_so_thuc()
            print("Nhap luong thuc an (kg/ngay): ", end="")
            monkey_food_amount = nhap_so_thuc()

            sv_monkey = Monkey(monkey_name, monkey_age, monkey_food_amount)
            system_zoo.them_dong_vat(sv_monkey)

        else: 
            print(f"Loi! Vui long nhap lai")

    dv_thit = system_zoo.danh_sach_theo_loai_thuc_an('Thit')
    dv_thuc_vat = system_zoo.danh_sach_theo_loai_thuc_an('Thuc vat')

    print(f"\n\nSo thu {zoo_name} \n")
    print(f"Tong thuc an can thiet: {system_zoo.tong_thuc_an_can_thiet()} (kg/ ngay)")
    print(f"Danh sach dong vat an thit: {dv_thit}")
    print(f"Danh sach dong vat an thuc vat: {dv_thuc_vat}")
    print(f"Tat ca keu len: ")
    system_zoo.tat_ca_keu()

    system_zoo.luu_file('EX15_1.txt')

main()
