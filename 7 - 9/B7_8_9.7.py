
try:
    f = open('diem.txt','r')
    content = f.read()
    print(content)
except FileNotFoundError:
    print('Khong tim thay file, tao file moi...')
    with open('diem.txt', 'w') as f:
        f.write('Hello anh chi em\n')
        f.write('Minh dang hoc Python\n')
finally:
    print('Ket thuc chuong trinh!')
    