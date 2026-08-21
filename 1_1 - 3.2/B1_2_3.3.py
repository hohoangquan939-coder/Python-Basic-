#Tinh tong cac chu so nguyen

n = int(input("Nhap so nguyen: "))

result = 0
k = n
while(k > 0):
    result += k%10
    k = k // 10

print(f"Tong cac chu so cua {n} la: {result}")