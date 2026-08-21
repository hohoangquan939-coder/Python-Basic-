# If - ELSE

x = float(input("Nhap so: "))

if x>0:
    print("Positive")
elif x<0:
    print("Negative")
else:
    print("Zero")


score = float(input("Nhap diem: "))

if score >= 9:
    print("Xuat sac")
elif score >= 7:
    print("Kha")
elif score >= 5:
    print("Trung binh")
else:
    print("Yeu")
