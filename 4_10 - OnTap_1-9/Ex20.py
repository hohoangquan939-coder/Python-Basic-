
def kiem_tra_diem(x):
    try: 
        x = float(x)
        if not (x>=0 and x<=10): 
            print(f"Loi: diem phai trong khoang 0-10!")
            return False
        else: return True
    except ValueError: 
        print(f"Loi: diem phai la so!")
        return False

def nhap_thong_tin():
    lst_danh_sach = []
    while(True):
        ten = input("Nhap ten (hoac 'end'): ")
        if ten == 'end': break
        diem = input("Nhap diem: ")
        while not kiem_tra_diem(diem): 
            diem = input('Nhap diem:')
        
        k = {
            'name': ten,
            'score': float(diem),
            'rank': ''
        }
        lst_danh_sach.append(k)
    return lst_danh_sach


def diem_trung_binh(lst_danh_sach):
    average = 0
    for i in lst_danh_sach:
        average += i['score']
    return average/len(lst_danh_sach)


def xep_loai(sinh_vien):
    if sinh_vien['score'] >= 8: return 'Gioi'
    elif sinh_vien['score'] >= 6.5: return 'Kha'
    elif sinh_vien['score'] >= 5: return 'Trung binh'
    else: return 'Yeu'


def diem_cao_nhat(lst_danh_sach):
    max_name = lst_danh_sach[0]['name']
    max_score = lst_danh_sach[0]['score']
    max_rank = lst_danh_sach[0]['rank']

    for i in lst_danh_sach:
        if i['score'] > max_score: 
            max_score = i['score']
            max_name = i['name']
            max_rank = i['rank']

    return max_name, max_score, max_rank

def ghi_vao_file(lst_danh_sach):
    with open("ketqua.txt", "w") as f:
        for i in lst_danh_sach:
           f.write(f"{i['name']} - {i['score']} diem - {i['rank']}\n")

def main():
    lst_danh_sach = nhap_thong_tin()
    if not lst_danh_sach:
        print("Khong co du lieu!")
        return
    
    diem_tb = diem_trung_binh(lst_danh_sach)

    for i in lst_danh_sach:
        hang = xep_loai(i)
        i['rank'] = hang
    ghi_vao_file(lst_danh_sach)

    ten, diem, hang = diem_cao_nhat(lst_danh_sach)


    print(f"Diem trung binh ca lop: {diem_tb}")
    print(f"Da ghi ket qua vao file ketqua.txt")
    print(f"Sinh vien cao nhat: {ten} - {diem} diem - {hang}")

main()