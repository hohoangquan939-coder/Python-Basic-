from abc import ABC, abstractmethod

class MenuItem(ABC):
    def __init__(self, name, base_price):
        self.name = name
        self.__base_price = base_price
    
    @abstractmethod
    def tinh_gia(self):
        pass

    @abstractmethod
    def thong_tin(self): # Mo ta mon an
        pass

    def get_price(self):
        return self.__base_price

    def set_price(self, price):
        if price < 0: 
            print(f"Gia mon an khong the be hon 0")
        else:
            self.__base_price = price


class FoodItem(MenuItem):
    def __init__(self, name, base_price, is_spicy):
        super().__init__(name, base_price)
        self.is_spicy = is_spicy

    def thong_tin(self):
        print(f"Ten mon: {self.name:<15}     - {'Cay' if self.is_spicy else 'Khong cay':<15}       - Gia: {self.tinh_gia():<10} ")

    def tinh_gia(self):
        if self.is_spicy == True:
            return self.get_price() + 5000
        else:
            return self.get_price()


class DrinkItem(MenuItem):
    def __init__(self, name, base_price, size):
        super().__init__(name, base_price)
        self.size = size
    
    def thong_tin(self):
        print(f"Ten do uong: {self.name:<15} - Size: {self.size:<15} - Gia: {self.tinh_gia():<10}")

    def tinh_gia(self):
        if self.size == 'M': 
            return self.get_price()
        elif self.size == 'S':
            return self.get_price() - 5000
        else:
            return self.get_price() + 10000
    

class ComboItem(MenuItem):
    def __init__(self, name):
        super().__init__(name, 0)
        self.__combo_items = []
    
    def them_mon(self, item):
        self.__combo_items.append(item)

    def get_combo_items(self):
        return self.__combo_items
    
    def tinh_gia(self):
        total = 0
        for item in self.__combo_items:
            total += item.tinh_gia()
        return total * 0.85
    
    def thong_tin(self):
        print(f"Ten combo: {self.name}")
        for item in self.__combo_items:
            item.thong_tin()
        print(f"Tong gia tien cua {self.name} (Giam gia 15%): {self.tinh_gia()}")


class Order:
    def __init__(self):
        self.__items = []
    
    def them_mon(self, mon):
        self.__items.append(mon)
    
    def tinh_tong_tien(self):
        total = 0
        for item in self.__items:
            total += item.tinh_gia()
        return total

    def in_hoa_don(self):
        print(f"----------------------------------------------------------------------")
        print(f"                               Hoa don                                ")
        print(f"----------------------------------------------------------------------")
        for item in self.__items:
            item.thong_tin()
            print(f"----------------------------------------------------------------------")
        print(f"\nTong gia tien: {self.tinh_tong_tien()}")


class Restaurant:

    def __init__(self, name):
        self.name = name
        self.__menu = []
    
    def them_vao_menu(self, item):
        self.__menu.append(item)
    
    def tim_mon_theo_ten(self, name):
        for item in self.__menu:
            if item.name == name:
                return item
        return None 
    
    def danh_sach_mon_an(self):
        lst_mon_an = []
        for item in self.__menu:
            if isinstance(item, FoodItem):
                lst_mon_an.append(item)
        return lst_mon_an

    def danh_sach_nuoc_uong(self):
        lst_nuoc_uong = []
        for item in self.__menu:
            if isinstance(item, DrinkItem):
                lst_nuoc_uong.append(item)
        return lst_nuoc_uong

    def danh_sach_combo(self):
        lst_combo = []
        for item in self.__menu:
            if isinstance(item, ComboItem):
                lst_combo.append(item)
        return lst_combo   

    def luu_menu(self, filename):
        with open(filename, 'w') as f:
            f.write(f"Ten nha hang: {self.name}\n")
            f.write(f"Menu quan\n")
            lst_food = self.danh_sach_mon_an()
            lst_drink = self.danh_sach_nuoc_uong()
            lst_combo = self.danh_sach_combo()

            f.write(f"----------------------------------------------------------------------\n")
            f.write(f"Mon an\n")
            f.write(f"----------------------------------------------------------------------\n")
            for item in lst_food:
                f.write(f"Ten mon: {item.name:<15}     - {'Cay' if item.is_spicy else 'Khong cay':<15}       - Gia: {item.tinh_gia():<10}\n")

            f.write(f"----------------------------------------------------------------------\n")
            f.write(f"Do uong\n")
            f.write(f"----------------------------------------------------------------------\n")
            for item in lst_drink:
                f.write(f"Ten do uong: {item.name:<15} - Size: {item.size:<15} - Gia: {item.tinh_gia():<10}\n")
            
            f.write(f"----------------------------------------------------------------------\n")
            f.write(f"Combo\n")
            f.write(f"----------------------------------------------------------------------\n")
            for item in lst_combo:
                f.write(f"Ten combo: {item.name}\n")
                mon_trong_combo = item.get_combo_items()
                for dish in mon_trong_combo:
                    if isinstance(dish, FoodItem):
                        f.write(f"Ten mon: {dish.name:<15}     - {'Cay' if dish.is_spicy else 'Khong cay':<15}       - Gia: {dish.tinh_gia():<10}\n")
                    else:
                        f.write(f"Ten do uong: {dish.name:<15} - Size: {dish.size:<15} - Gia: {dish.tinh_gia():<10}\n")
                f.write(f"Tong gia tien cua combo (Giam gia 15%): {item.tinh_gia()}\n\n")

    def doc_menu(self, filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    print(line.strip())
        except FileNotFoundError:
            print(f"Khong mo duoc file")


def test_co_san():
    menu = [
    FoodItem('Mi cay',  45000, True),
    FoodItem("Ga ran", 50000, True),
    FoodItem("Com chien", 45000, False),
    FoodItem("Mi xao", 40000, True),
    FoodItem("Pho bo", 55000, False),
    FoodItem("Pizza", 120000, True),
    FoodItem('Xuc xich', 15000, False),
    FoodItem('Ca vien chien', 25000, True),
    DrinkItem("Coca", 20000, "S"),
    DrinkItem("Pepsi", 20000, "M"),
    DrinkItem("Tra dao", 30000, "L"),
    DrinkItem("Tra sua", 35000, "M"),
    DrinkItem("Cam ep", 40000, "L"),
    ] #13
    
    combo = [
        ComboItem('Combo 1'),
        ComboItem('Combo 2')
    ]

    combo[0].them_mon(menu[1])
    combo[0].them_mon(menu[2])
    combo[0].them_mon(menu[10])

    combo[1].them_mon(menu[2])
    combo[1].them_mon(menu[3])
    combo[1].them_mon(menu[5])
    combo[1].them_mon(menu[8])

    r1 = Restaurant('Quan An Vat')
    for item in menu:
        r1.them_vao_menu(item)
    r1.them_vao_menu(combo[0])
    r1.them_vao_menu(combo[1])

    r1.luu_menu('EX15_4.txt')
    r1.doc_menu('EX15_4.txt')


    od1 = Order()
    while True:
        dish = input(f"Hay nhap ten mon muon order (Mon an / Thuc uong / Combo / Done): ")
        if dish == "Done": break

        item = r1.tim_mon_theo_ten(dish)
        if item==None:
            print(f"Khong co mon nay! Vui long chon lai")
        else:
            od1.them_mon(item)

    od1.in_hoa_don()

test_co_san()