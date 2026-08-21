
def kiem_tra_so(a):
    if a==0: print(f"So 0")
    elif a>0:
        print(f"So duong")
        if a%2==0: print(f"So chan")
        else: print(f"So le")
    else:
        print(f"So am")


a = int(input("Nhap n: "))
kiem_tra_so(a)