
def chia_an_toan(a, b):
    try:
        return round(a/b, 2)
    except ZeroDivisionError:
        return "Khong the chia cho 0"


def viet_hoa_dau_moi_tu(cau):
    res = ""
    if cau[0].isalpha():
        res += cau[0].upper()
    if res != "": start = 1
    else: start = 0
    for i in range(start, len(cau)):
        if cau[i].isalpha() and cau[i-1]==' ':
            res += cau[i].upper()
        else:
            res += cau[i]
    return res

def nhap_so_nguyen():
    while True:
        try:
            x = input("Nhap so nguyen: ")
            x = int(x)
            return x
        except ValueError:
            print(f"Nhap khong hop le, thu lai")

def tach_am_duong(mang):
    negative_number = []
    positive_number = []
    for i in mang:
        if i == 0:
            continue
        elif i < 0:
            negative_number.append(i)
        else:
            positive_number.append(i)
    return positive_number, negative_number


def nen_chuoi(chuoi):
    res = ""
    i = 0
    while i < len(chuoi):
        count = 1
        res += chuoi[i]
        while (i+1) < len(chuoi) and chuoi[i] == chuoi[i+1]:
            i += 1
            count += 1
        res += str(count)
        i += 1
    return res


def main():
    print(f"Bai 1: {chia_an_toan(10,2)} ")
    print(f"Bai 2: {viet_hoa_dau_moi_tu('Chao ban toi la quan')}")
    print(f"Bai 3: {nhap_so_nguyen()}")
    po, ne = tach_am_duong([2,3,-2,0,4,1,2,4,5,6,2,3,4,5,0])
    print(f"Bai 4: Pos: {po} | Ne: {ne}")
    print(f"Bai 5: {nen_chuoi('aaabccccdeeeef')}")
main()