
def tinh_tong_nhap():
    total = 0

    while(True):
        i = input("Nhap so (hoac 'done' de dung): ")
        if i=='done': break

        try: total += int(i)
        except ValueError:
            print(f"Loi: khong phai la so, vui long nhap lai!")

    print(f"Tong cac so da nhap: {total}")

tinh_tong_nhap()