
class SanPham:
    def __init__(self, name, price, number):
        self.name = name
        self.price = price
        self.number = number
    
    def  tinh_tong_tien(self):
        return self.price * self.number

    def giam_gia(self, phantram):
        self.price = round(self.price * (1 - phantram/100), 2)
    
    def thong_tin(self):
        return f"Ten: {self.name } - Gia: {self.price} - So luong: {self.number}"

def main():
    a = SanPham('Ao', 100000, 3)
    print(f"Tong tien: {a.tinh_tong_tien()}")
    a.giam_gia(20)
    print(f"Gia sau khi giam: {a.price}")
    print(f"Thong tin san pham: {a.thong_tin()}")


main()