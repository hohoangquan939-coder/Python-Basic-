#Tam giac kim cuọng

n = int(input("Nhap cap tam giác (So le): "))

while( n%2 == 0):
    print("Chi duoc nhap so le")
    n = int(input("Vui long nhap lai: "))


for i in range(1, n+1, 2):
    print(" " * ((n-i)//2) + "*" * i)

for i in range(1, n+1):
    print(" " * i + "*" * (n - 2*i))

