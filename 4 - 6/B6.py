# def xinchao(name):
#     print(f"Hello {name} !")

# xinchao("Quan")


# def tong(a, b):
#     return a+b

# result = tong(2313,347234)
# print(f"Tong {result}")

# def thamso(name, macdinh = "Hello"):
#     print(f"{macdinh} {name}")

# thamso("Quan")
# thamso("Quan", "Chao")


# #Goi tham so khong can theo thu tu
# def info(name, age, city):
#     print(f"{name}, {age} tuoi, {city}")

# info(age=20, city = "Da Nang", name = "Quan")



def diemtb(a, b):
    return (a+b)/2

def xeploai(a):
    if( a >= 9): return "Gioi"
    elif( a >= 7): return "Kha"
    elif( a >= 5): return "Trung binh"
    else: return "Yeu"


lt = int(input("Nhap diem li thuyet: "))
tt = int(input("Nhap diem thuc hanh: "))


result = diemtb(lt, tt)
print(f"Diem trung binh: {result}")
print(f"Xep loai: {xeploai(result)}")