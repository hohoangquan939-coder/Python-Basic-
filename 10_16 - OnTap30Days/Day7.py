def ghi_file(filename, lst_dict):
    with open(filename, 'w') as f:
        for char in lst_dict:
            f.write(f"{char['ten']} - {char['tuoi']}\n")
        print(f"Da ghi file thanh cong")

def doc_file(filename):
    try:
        with open(filename, 'r') as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print(f"Loi! Khong tim thay file")

def lay_phan_tu(mang, idx):
    try:
        res = mang[idx]
        return res
    except IndexError:
        return f"Loi truy cap chi so vuot pham vi"

def tron_2_mang_da_sap_xep(a, b):
    i, j = 0, 0
    res = []
    while i<len(a) and j<len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    
    while i<len(a):
        res.append(a[i])
        i += 1
    
    while j<len(b):
        res.append(b[j])
        j += 1
    return res

def uoc_chung_lon_nhat(a, b):
    while b != 0:
        r = a%b 
        a = b
        b = r
    return a

def chuyen_so_thanh_chu(so):
    if so<0 or so>9:
        return f"So khong hop le"
    
    lst_res = ['khong', 'mot', 'hai', 'ba', 'bon', 'nam', 'sau', 'bay', 'tam', 'chin']
    return lst_res[so]

def main():
    print(f"Bai 1: ")
    ghi_file("sv.txt", [{"ten":"An","tuoi":20},{"ten":"Binh","tuoi":21}])
    doc_file("sv.txt")
    print(f"Bai 2: {lay_phan_tu([1,2,3], 2)}")
    print(f"Bai 3: {tron_2_mang_da_sap_xep([1,2,3,9], [3,4,5,6])}")
    print(f"Bai 4: {uoc_chung_lon_nhat(789012, 123456)}")
    print(f"Bai 5: {chuyen_so_thanh_chu(14)}")


main()
