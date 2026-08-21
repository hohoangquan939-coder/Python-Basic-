from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.__rental_price_per_day = rental_price_per_day
    
    @abstractmethod
    def tinh_phi_thue(self, days):
        pass

    @abstractmethod
    def loai_xe(self):
        pass

    def get_rental_price_per_day(self):
        return self.__rental_price_per_day

    def set_rental_price_per_day(self, price):
        if price < 0: 
            print(f"Gia thue xe hang ngay khong the be hon 0")
        else:
            self.__rental_price_per_day = price

    def thong_tin(self):
        print(f"Hang: {self.brand} - Model: {self.model} - Loai: {self.loai_xe()} - Gia thue: {self.__rental_price_per_day}/ngay")


class Motorbike(Vehicle):
    def __init__(self, brand, model, rental_price_per_day):
        super().__init__(brand, model, rental_price_per_day)
    
    def tinh_phi_thue(self, days):
        return days * self.get_rental_price_per_day()
    
    def loai_xe(self):
        return 'Xe may'


class Car(Vehicle):
    def __init__(self, brand, model, rental_price_per_day, num_seats):
        super().__init__(brand, model, rental_price_per_day)
        self.num_seats = num_seats

    def tinh_phi_thue(self, days):
        if days >= 7:
            return days * round( self.get_rental_price_per_day() * 0.9, 2)
        else:
            return days * self.get_rental_price_per_day()
        
    def loai_xe(self):
        return 'O to'
    

class Truck(Vehicle):
    def __init__(self, brand, model, rental_price_per_day, max_load_kg):
        super().__init__(brand, model, rental_price_per_day)
        self.max_load_kg = max_load_kg

    def tinh_phi_thue(self, days):
        return self.get_rental_price_per_day() * days + 200000
    
    def loai_xe(self):
        return 'Xe tai'
    

class Rental_Store:
    def __init__(self, name):
        self.name = name
        self.__vehicles = []

    def them_xe(self, vehicle):
        self.__vehicles.append(vehicle)

    def tim_xe_theo_loai(self, loai):
        lst = []
        for i in self.__vehicles:
            if i.loai_xe() == loai: 
                lst.append(i)
        return lst
    
    def xe_re_nhat(self):
        if not self.__vehicles:
            return None
        
        i = self.__vehicles[0]
        for j in self.__vehicles:
            if i.get_rental_price_per_day() > j.get_rental_price_per_day():
                i = j
        return i

    def tinh_tong_doanh_thu(self, danh_sach_thue):
        total = 0
        for vehicle, days in danh_sach_thue:
            total += vehicle.tinh_phi_thue(days)
        return total

    def luu_danh_sach_xe(self, filename):
        with open(filename, 'w') as f:
            f.write(f"Ten cua hang: {self.name}\n")
            for i in self.__vehicles:
                f.write(f"Loai xe: {i.loai_xe():<10} - "
                        f"Brand: {i.brand:<10} - Model: {i.model:<15} - "
                        f"Rental price per day: {i.get_rental_price_per_day():<10}\n")
    
    def doc_danh_sach_xe(self, filename):
        try:
            with open(filename, 'r') as f:
                for line in f:
                    print(line.strip())
        except FileNotFoundError:
            print(f"Loi! Khong tim thay File")


def input_float():
    while True:
        try:
            x = float(input())

            if x <= 0:
                raise Exception("Phai nhap so lon hon 0")
            
            return x
        
        except ValueError:
            print(f"Loi! Phai nhap so thuc")

        except Exception as e:
            print(str(e))

def input_int():
    while True:
        try:
            x = int(input())

            if x <= 0:
                raise Exception("Phai nhap so lon hon 0")
            
            return x
        
        except ValueError:
            print(f"Loi! Phai nhap so nguyen")

        except Exception as e:
            print(str(e))

def main():
    # store_name = input("Nhap ten cua cua hang: ")
    # lst_vehicles = []
    # Store1 = Rental_Store(store_name, lst_vehicles)

    # while True:
    #     vehicle_type = input("Nhap loai xe (xe may/o to/xe tai/end): ")

    #     if vehicle_type == "end": 
    #         break
        
    #     elif vehicle_type == 'xe may' or vehicle_type == 'o to' or vehicle_type == 'xe tai':
    #         brand = input("Nhap hang xe: ")
    #         model = input("Nhap mau xe: ")
    #         print(f"Nhap tien thue moi ngay (VND/ngay): ", end = "")
    #         price_per_day = input_float()

    #         if vehicle_type == 'xe may':
    #             xe = Motorbike(brand, model, price_per_day)

    #         elif vehicle_type == 'o to':
    #             print(f"Nhap so luong ghe: ", end = "")
    #             number_seats = input_int()
    #             xe = Car(brand, model, price_per_day, number_seats)

    #         elif vehicle_type == 'xe tai':
    #             print(f"Nhap khoi luong cho duoc toi da (kg): ", end = "")
    #             max_load = input_float()
    #             xe = Truck(brand, model, price_per_day, max_load)
            
    #         Store1.them_xe(xe)

    #     else:
    #         print(f"Lua chon khong hop le! Vui long nhap lai")

    # # Da xong vong While
    Store = Rental_Store("Yeah")

    car1 = Car("Toyota", "Vios", 500000, 5)
    car2 = Car("Honda", "Civic", 650000, 5)
    car3 = Car("Hyundai", "Accent", 450000, 5)
    car4 = Car("Mazda", "CX-5", 900000, 7)

    moto1 = Motorbike("Honda", "Wave Alpha", 100000)
    moto2 = Motorbike("Yamaha", "Exciter 155", 180000)
    moto3 = Motorbike("Suzuki", "Raider", 170000)

    truck1 = Truck("Hino", "300", 1200000, 5000)
    truck2 = Truck("Isuzu", "NQR75", 1500000, 7000)
    truck3 = Truck("Hyundai", "Mighty", 1800000, 8000)

    lst_danh_sach_xe_cua_hang = [
        car1,
        car2,
        car3,
        car4,
        moto1,
        moto2,
        moto3,
        truck1,
        truck2,
        truck3
    ]

    lst_danh_sach_thue_xe = [
        (car1, 5),     # Car
        (moto1, 2),    # Motorbike
        (truck1, 1)    # Truck
    ]

    for i in lst_danh_sach_xe_cua_hang:
        Store.them_xe(i)
    
    Store.luu_danh_sach_xe("EX15_2.txt")
    Store.doc_danh_sach_xe("EX15_2.txt")

    print(f"\nDanh sach xe dang thue: ")
    for i in lst_danh_sach_thue_xe:
        print(f"Hang: {i[0].brand:<10} - Loai: {i[0].loai_xe():<10} - Ngay thue: {i[1]:<3}")
    print(f"Tong danh thu: {Store.tinh_tong_doanh_thu(lst_danh_sach_thue_xe)}")

    
main()
