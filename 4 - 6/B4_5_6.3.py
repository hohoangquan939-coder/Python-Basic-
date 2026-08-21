data = [ 
    { "name":"Quan", "age": 20, "score": 8.5 },
    { "name":"An", "age": 21, "score": 9.2 },
    { "name":"Binh", "age":21, "score":4.5}
]


def xeploai(x):
    if x >= 9 : return "Gioi"
    elif x >= 7: return "Kha"
    elif x >= 5: return "Trung binh"
    else: return "Yeu"


def show_list(lst):
    for i in range(len(lst)):
        print(f"{i+1}. {lst[i]['name']} - {lst[i]['age']} tuoi - {lst[i]['score']} diem - {xeploai(lst[i]['score'])}")


def search_max_score(lst):
    sv_max = lst[0]
    for i in range(len(lst)):
        if lst[i]['score'] > sv_max['score']: sv_max = lst[i]

    return sv_max


show_list(data)
sv_maxd = search_max_score(data)
print(f"Sinh vien gioi nhat: {sv_maxd['name']} - {sv_maxd['score']} diem")