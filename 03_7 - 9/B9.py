# Loi nhap so 
try:
    n = int(input("Nhap so:"))
    print(f"So vua nhap: {n}")
except ValueError:
    print("Loi: Phai nhap so nguyen!")


try:
    n = int(input("Nhap so: "))
    result = 10/n
    print(result)
except ValueError:
    print("Phai nhap so!")
except ZeroDivisionError:
    print("Khong chia duoc cho 0!")


try:
    f = open('test.txt', 'r')
    content = f.read()
except FileNotFoundError:
    print("Khong tim thay file!")
finally:
    print('Xong')