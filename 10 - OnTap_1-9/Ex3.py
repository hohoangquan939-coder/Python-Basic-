
def tong_ba_nam(a, b):
    sum = 0
    for i in range(a,b+1):
        if i%3==0 or i%5==0: sum += i
    return sum

a = int(input("Nhap a: "))
b = int(input("Nhap b: "))

res = tong_ba_nam(a,b)
print(f"Tong cac so chia het cho 3 hoac 5: {res}")