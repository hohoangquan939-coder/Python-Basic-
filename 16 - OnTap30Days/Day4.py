def dao_key_value(d):
    res = {}
    for key, value in d.items():
        res[value] = key
    return res


def xoay_mang(mang, k):
    res = []
    if k>len(mang) or k<0:
        return res
    for i in range(len(mang)-k, len(mang)):
        res.append(mang[i])
    for i in range(0, len(mang)-k):
        res.append(mang[i])
    return res


def doc_file(filename):
    try:
        with open(filename, 'r') as f :
            count = 0
            for line in f:
                count += 1
        return count
    except FileNotFoundError:
        return (f"File khong ton tai")


def so_nguyen_to(b):
    a = b
    if a <= 1: return False
    if a==2: return True
    a = int(a**0.5) + 1
    for i in range(2, a):
        if b%i == 0: return False
    return True


def so_nguyen_to_trong_khoang(a, b):
    lst_res = []
    for i in range(a, b+1):
        if so_nguyen_to(i): lst_res.append(i)
    return lst_res


def dem_nguyen_am(chuoi):
    chuoi = chuoi.lower()
    res = 0
    for i in range(0, len(chuoi)):
        if chuoi[i] in ['a', 'e', 'u', 'o', 'i']:
            res += 1
    return res

def main():
    print(f"Bai 1: {dao_key_value({"a":1, "b":2})}")
    print(f"Bai 2: {xoay_mang([1,2,3,4,5,6,7,8,9], 3)}")
    print(f"Bai 3: {doc_file('data.txt')}")
    print(f"Bai 4: {so_nguyen_to_trong_khoang(0, 30)}")
    print(f"Bai 5: {dem_nguyen_am('xin chao ban! MInh ten la QUAN')}")

main()