
s = input('Nhap chuoi: ')
chu, so, space, ki_tu = 0, 0, 0, 0

for i in s:
    if i.isdigit(): so += 1
    elif i.isalpha(): chu += 1
    elif i == ' ': space += 1
    else: ki_tu += 1

print(f"So chu cai: {chu}")
print(f"So so: {so}")
print(f"So khoang trang: {space}")
print(f"So ky tu dac biet: {ki_tu}")