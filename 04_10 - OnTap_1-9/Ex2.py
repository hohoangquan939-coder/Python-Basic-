
def phuong_trinh_bac_nhat(a, b):
    if a==0 and b==0: print(f"Phuong trinh vo so nghiem")
    elif a==0: print(f"Phuong trinh vo nghiem")
    else: print(f"Nghiem: x = {round(-b/a, 2)}")    



a = float(input("Nhap a: "))
b = float(input("Nhap b: "))

phuong_trinh_bac_nhat(a, b)