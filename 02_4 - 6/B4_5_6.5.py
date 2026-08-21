
data = [
    {"name": "Quan", "score":7},
    {"name": "Hanh", "score":9},
    {"name": "Thinh", "score":8.4},
    {"name": "Lan", "score":10},
    {"name": "Ngoc", "score":5.2},
    {"name": "Linh", "score":3},
    {"name": "Hung", "score":2.6}
]


def diem_tb(lst):
    diem = 0
    so = 0
    for i in lst:
        diem += i['score']
        so += 1
    return round(diem/so, 2)

def xep_loai(x):
    if x >= 9: return "Gioi"
    elif x >= 7: return "Kha"
    elif x >= 5: return "Trung binh" 
    else: return "Yeu"

def loc_theo_loai(lst, loai):
    res = []
    for sv in lst:
        if(xep_loai(sv['score']) == loai): res.append(sv['name'])
    return res

def show_list(lst):
    for i in range(len(lst)):
        print(lst[i], end = "")
        if i != len(lst)-1: print(", ", end = "")
        else: print(".", end = "")
    print("")


gioi = loc_theo_loai(data, "Gioi")
kha = loc_theo_loai(data, "Kha")
tbinh = loc_theo_loai(data, "Trung binh")
yeu = loc_theo_loai(data, "Yeu")


print("Diem trung binh ca lop", diem_tb(data))
print("Cac hoc sinh gioi: ", end = "") 
show_list(gioi)
print("Cac hoc sinh kha: ", end = "")
show_list(kha)
print("Cac hoc sinh trung binh: ", end = "")
show_list(tbinh)
print("Cac hoc sinh yeu: ", end = "")
show_list(yeu)