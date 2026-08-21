
def diem_trung_binh(sv):
    diem = (sv['toan'] + sv['ly'] + sv['hoa']) / 3
    return round(diem, 2)

def in_xep_loai(diem):
    if diem>=8: return("Gioi")
    elif diem>=6.5: return("Kha")
    elif diem>=5: return("Trung binh")
    else: return("Yeu")

sinh_vien = {
    "name": "Tran Van A",
    "toan": 8.5 ,
    "ly": 7.0,
    "hoa": 9.0
}

diem_tb = diem_trung_binh(sinh_vien)

print(f"Sinh vien: {sinh_vien['name']}")
print(f"Diem trung binh: {diem_tb}")

print(f"Xep loai: {in_xep_loai(diem_tb)}")