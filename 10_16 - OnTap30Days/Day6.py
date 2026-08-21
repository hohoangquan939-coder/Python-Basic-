def tim_phan_tu_xuat_hien_nhieu_nhat(mang):
    dict_count = {}
    for i in mang:
        if i not in dict_count:
            dict_count[i] = 1
        else:
            dict_count[i] += 1
    key_max = -1
    value_max = -1
    for key, value in dict_count.items():
        if value_max == -1:
            key_max = key
            value_max = value
        
        if value > value_max:
            value_max = value
            key_max = key
        
    return key_max


def kiem_tra_anagram_1(s1, s2):
    return sorted(s1) == sorted(s2)

def kiem_tra_anagram_2(s1, s2):
    dict_count = {}
    for c in range(0, len(s1)):
        if s1[c] not in dict_count:
            dict_count[s1[c]] = 1
        else:
            dict_count[s1[c]] += 1

    for c in range(0, len(s2)):
        if s2[c] not in dict_count or dict_count[s2[c]] == 0:
            return False
        else:
            dict_count[s2[c]] -= 1
            if dict_count[s2[c]] == 0:
                del dict_count[s2[c]]
    
    return dict_count == {}
    
def fibonacci(n):
    if n <= 0: return []
    lst_res = [0]
    if n >= 2: 
        lst_res.append(1)
    i = 2
    while n-2 > 0:
        lst_res.append(lst_res[i-1] + lst_res[i-2])
        i += 1
        n -= 1
    return lst_res

def dem_so_lan_xuat_hien(mang):
    dict_res = {}
    for i in mang:
        if i not in dict_res:
            dict_res[i] = 1
        else:
            dict_res[i] += 1
    return dict_res

def xoa_ki_tu_trung(chuoi):
    res = ""
    i = 0
    while i < len(chuoi):
        res += chuoi[i]
        while i+1 < len(chuoi) and chuoi[i] == chuoi[i+1]:
            i += 1
        i += 1
    return res


def main():
    print(f"Bai 1: {tim_phan_tu_xuat_hien_nhieu_nhat([1,3,2,3,3,1])}")
    print(f"Bai 2.1: {kiem_tra_anagram_1('listen', 'silent')}")
    print(f"Bai 2.2: {kiem_tra_anagram_2('hello', 'llohe')}")
    print(f"Bai 3: {fibonacci(8)}")
    print(f"Bai 4: {dem_so_lan_xuat_hien([1,2,2,3,1,1])}")
    print(f"Bai 5: {xoa_ki_tu_trung('aaaaabbbbbbbbbbcdddddddddd')}")

main()