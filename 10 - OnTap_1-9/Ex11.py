
def dem_tu(s):
    res = {}
    lst_s = s.split()
    for i in lst_s:
        i = i.lower()
        if i in res: res[i] += 1
        else: res[i] = 1
    
    return res


s = input("Nhap cau: ")
ket_qua = dem_tu(s)
print(ket_qua)
