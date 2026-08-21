#Kiem tra so nguyen to

n = int(input("Nhap so n: "))

k = True
for i in range(2, int(n**0.5)+1):
    if n%i == 0: 
        k = False
        break
    
if k: print("Day la so nguyen to")
else: print("Day khong la so nguyen to")
    
    
