
def kiem_tra_so_nguyen_to(a):
    if a<2: return False
    for i in range(2, int(a**0.5) + 1):
        if a%i==0: return False
    return True

def so_nguyen_to(a, b, ket_qua):
    total = 0
    for i in range(a, b+1):
        if kiem_tra_so_nguyen_to(i): 
            ket_qua.append(i)
            total += 1
    return total

a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
ket_qua = []
c = so_nguyen_to(a, b, ket_qua)

print(f"Cac so nguyen to: {ket_qua}") 
print(f"So luong: {c}")

