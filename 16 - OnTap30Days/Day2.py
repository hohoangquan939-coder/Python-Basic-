# Day 2

# Gop 2 mang da sap xep thanh 1 mang duoc sap xep
def gop_2_mang_khong_trung_sap_xep(a, b):
    lst_res = []
    i, j = 0, 0
    while i<len(a) and j<len(b):
        if a[i] <= b[j]:
            lst_res.append(a[i])
            i += 1
        else:
            lst_res.append(b[j])
            j += 1
    
    while i < len(a):
        lst_res.append(a[i])
        i += 1
    
    while j < len(b):
        lst_res.append(b[j])
        j += 1
    
    return lst_res


# Gop 2 mang theo thu tu xuat hien
def gop_2_mang_khong_trung(a, b):
    lst_res = []
    for x in a:
        if x not in lst_res:
            lst_res.append(x)
    for x in b:
        if x not in lst_res:
            lst_res.append(x)
    return lst_res


# Tim value lon nhat trong dictionary va tra ve key
def tim_gia_tri_lon_nhat(a):
    object = None
    for x in a:
        if object == None:
            object = x
        else:
            if a[object] < a[x]:
                object = x
    return object


# Doc file diem va tra ve diem trung binh
def doc_file_diem_trung_binh():
    try:
        with open("diem.txt", 'r') as f:
            total = 0
            count = 0
            for line in f:
                lst_data = line.strip().split(',')
                grade = float(lst_data[1])
                total += grade
                count +=1

            if count > 0:
                avg = round(total/count, 2)
            else:
                avg = 0

            with open("Ketqua.txt", 'w') as f:
                f.write(f"Diem trung binh: {avg}\n")

    except FileNotFoundError:
        print(f"Khong mo duoc file")


# Nhom theo do dai
def nhom_theo_do_dai(ds_tu):
    dic_res = {}
    for word in ds_tu:
        n = len(word)
        if n not in dic_res:
            dic_res[n] = [word]
        else:
            dic_res[len(word)].append(word)
    return dic_res


def kiem_tra_palindrome(s):
    print(f"Ban nhap chuoi: {s}")
    s = ''.join(s.strip().split())
    s = s.upper()
    i, j = 0, len(s)-1
    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def main():
    lst = gop_2_mang_khong_trung([1,2,3,4,4], [4,3,1, 4,5,6,7])
    print(f"Bai 1: ", lst)
    object = tim_gia_tri_lon_nhat({"a":3, "b":9, "c":5})
    print(f"Bai 2: ", object)
    doc_file_diem_trung_binh()
    print(f"Bai 3: Hoan thanh")
    print(f"Bai 4: ", nhom_theo_do_dai(["meo", "cho", "voi", "ga"]))
    print(f"Bai 5: ", kiem_tra_palindrome("A man    a plan a canal Panama"))

main()