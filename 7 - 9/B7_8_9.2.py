
s = input("Nhap chuoi ki tu: ")

so, chu, cach, db, na, pa= 0, 0, 0, 0, 0, 0

for i in s:

    if i.isdigit(): so += 1
    elif i.isalpha(): 
        chu += 1
        c = i.lower()
        if c in 'aeuoi': na+=1
    elif i == ' ': cach += 1
    else: db += 1

pa = chu - na

print("Ki tu: ", s)
print("\nSo luong chu so: ", so)
print("So luong chu cai: ", chu)
print("So luong khoang trang: ", cach)
print("So luong ki tu dac biet: ", db)
print("Dao nguoc chuoi: ", s[::-1])
print("So luong nguyen am: ", na)
print("So luong phu am: ", pa)
