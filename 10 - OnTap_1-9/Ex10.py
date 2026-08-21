
products = [
    {"name": "Ban phim", "price": 250000},
    {"name": "Chuot", "price": 150000},
    {"name": "Man hinh", "price": 2500000},
    {"name": "Tai nghe", "price": 350000}
]

def loc_gia(lst, limit):
    result = []
    for i in lst:
        if i['price'] <= limit: result.append(i['name'])
    return result

limit = int(input("Nhap muc gia toi da: "))
ketqua = loc_gia(products, limit)
print(f"San pham phu hop: {ketqua}")