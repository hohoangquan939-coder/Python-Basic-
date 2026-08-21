class Student:
    def __init__(self, name, age): #constructor: function tu dong chay
        self.name = name
        self.age = age

    def gioi_thieu(self):
        print(f"Toi ten la {self.name}, {self.age} tuoi")

s1 = Student("Quan", 19)
s1.gioi_thieu()

print(f"BAI TAP")

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def tong_tien(self):
        return self.quantity * self.price
    
    def thong_tin(self):
        print(f"Ten: {self.name} - Gia: {self.price} - SL: {self.quantity} - Tong: {self.tong_tien()}")


s1 = Product("May hut bui", 190000, 21)
s2 = Product("Kem danh rang", 15000, 102)

s1.thong_tin()
s2.thong_tin()