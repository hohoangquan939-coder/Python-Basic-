#Bai tap cho phan: Nhap xuat + Dieu kien + Vong lap
#In bang cuu chuong tu 1->10
def hople(a):
    return 1 <= a <= 10


n = int(input("Nhap so n: "))

while not (hople(n)):
    print("Khong hop le !")
    n = int(input("Vui long nhap lai so n: "))


for i in range(1,11):
    print(f"{n} x {i} = {n*i}")