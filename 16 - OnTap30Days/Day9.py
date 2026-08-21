
def gop_dict(d1, d2):
    d_res = {}
    for key, value in d1.items():
        if key not in d_res:
            d_res[key] = value
        else:
            d_res[key] += value

    for key, value in d2.items():
        if key not in d_res:
            d_res[key] = value
        else:
            d_res[key] += value

    return d_res

def sap_xep_theo_tang_suat(mang):
    dct = {}
    for i in mang:
        if i not in dct:
            dct[i] = 1
        else:
            dct[i] += 1

    lst_res = []

    for so,dem in sorted(dct.items(), key=lambda x:x[1], reverse = True):
        lst_res.extend([so] * dem)
    
    return lst_res

def chuyen_doi_an_toan(so):
    try:
        x = int(so)
        return x
    except ValueError:
        return 0

def dem_tan_suat_tu(doan_van):
    tan_suat = {}

    cac_tu = doan_van.split()

    for tu in cac_tu:
        if tu in tan_suat:
            tan_suat[tu] += 1
        else:
            tan_suat[tu] = 1

    return tan_suat


def chia_mang_thanh_nhom(mang, k):
    if k > len(mang):
        return []
    
    lst_res = []
    i = 0
    cur_lst = []
    while i < len(mang):
        if i!=0 and i%k == 0:
            lst_res.append(cur_lst)
            cur_lst = []
            cur_lst.append(mang[i])
        else:
            cur_lst.append(mang[i])
        i += 1
    if cur_lst:
        lst_res.append(cur_lst)

    return lst_res




def main():
    print(f"Bai 1: {gop_dict({'a':1,'b':2}, {'b':3,'c':4})}")
    print(f"Bai 2: {sap_xep_theo_tang_suat([1,1,2,2,3,3,3,3])}")
    print(f"Bai 3: {chuyen_doi_an_toan('abc')}")
    print(f"Bai 4: {dem_tan_suat_tu('Toi la toi ban la ban')}")
    print(f"Bai 5: {chia_mang_thanh_nhom([1,2,3,4,5,6,7], 3)}")



main()