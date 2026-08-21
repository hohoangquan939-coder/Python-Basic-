
n = int(input("Nhap so tang cua tam giac sao: "))

print("\nTam giac thuan - trai: ")
for i in range(1, n+1): # 0 -> n-1
    print("*" * i)


print("\nTam giac nguoc - trai: ")
for i in range(1, n+1): # 0 -> n-1
    print("*" * (n+1-i))


print("\nTam giac thuan - phai: ")
for i in range(1, n+1):
    print(" " * (n-i) + "*"* (i))


print("\nTam giac nguoc - phai: ")
for i in range(1, n+1):
    print(" " * (i-1) + "*" * (n+1-i))