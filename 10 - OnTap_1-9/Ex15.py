
def show_menu():
    print(f"1. Them so dien thoai ")
    print(f"2. Hien thi danh sach thue bao")
    print(f"3. Thoat chuong trinh")
    print(f"-------------------------")
    k = int(input(f"Nhap 1-3 de lua chon: "))
    return k

def them_so_dien_thoai():
    print("\n\n")
    f = open("lienlac.txt", "a")
    while(True):
        name = input("Nhap ten (hoac 'stop' de dung): ")
        if name == 'stop': break
        sdt = input("Nhap SDT:")
        f.write(f"{name} - {sdt}\n")
    f.close()
    print(f"Da luu vao file!")

def hien_thi_danh_sach_thue_bao():
    print(f"\n\n--- DANH BA ---")
    f = open("lienlac.txt", "r")
    content = f.read()
    print(content)
    f.close()

def main():
    while(True):
        k = show_menu()
        if k==1: them_so_dien_thoai()
        elif k==2: hien_thi_danh_sach_thue_bao()
        else: break


main()