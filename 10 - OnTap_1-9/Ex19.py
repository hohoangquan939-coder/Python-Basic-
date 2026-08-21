def tong_gia_tri(kho):
    total = 0
    for i in kho:
        total += i['soluong'] * i['gia']
    return total

def hang_het(kho):
    lst = []
    for i in kho:
        if i['soluong']==0: lst.append(i['ten'])
    return lst

kho = [
    {"ten": "Gao", "soluong": 50, "gia": 15000},
    {"ten": "Duong", "soluong": 0, "gia": 20000},
    {"ten": "Muoi", "soluong": 30, "gia": 5000}
]

total = tong_gia_tri(kho)
lst_het_hang = hang_het(kho)
with open('het_hang.txt', 'w') as f:
    for i in lst_het_hang:
        f.write(f"{i}\n")

print(f'Tong gia tri kho: {total}')
print(f'Hang het: {lst_het_hang}')
print(f'Da ghi vao file het_hang.txt')