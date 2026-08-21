
contacts = [
    {
        "name": "ho hoang Quan",
        "phone": '0329223448',
        "email": "hohoangquan939@gmail.com"
    },
    {
        "name": "nguyen vAN Hung",
        "phone": '0320983448',
        "email": "hungdepchai@gmail.com"   
    },
    {
        "name": "LE ThI Nhi",
        "phone": '0974223448',
        "email": "nhixinhgai@gmail.com"
    }
]

def chuanhoa_ten(cts):
    for i in cts:
        i['name'] = ' '.join(i['name'].title().split())
    return cts


def tim_ten(cts, key):
    res = []
    for i in cts:
        if(key.lower() in i['name'].lower() ): res.append(i)

    return res


def show_danhba(cts):
    count = 1
    cts = chuanhoa_ten(cts)
    for i in cts:
        print(f"{count}. {i['name']} | {i['phone']} | {i['email']}")
        count += 1

keyword = input("Nhap ten can tim: ")
ket_qua = tim_ten(contacts, keyword)
print(f'\nKet qua tim kiem "{keyword}":')
show_danhba(ket_qua)

