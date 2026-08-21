def loc_trung(lst):
    kq = []

    for x in lst:
        if x not in kq:
            kq.append(x)

    return kq

lst = list(map(int, input("Nhap day so: ").split()))
print(loc_trung(lst))

