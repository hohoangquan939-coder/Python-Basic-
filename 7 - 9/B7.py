
s1 = 'hello'
s2 = "hello"


s = 'hoc python'
s = 'H' + s[1:] # Thay s[1] = 'H'

print(s)
print(s[0])
print(s[1])
print(s[-1]) # Ki tu cuoi
print(s[len(s)-1])

print('\nIn tung chu bang for')
for i in s:
    print(i)


# s[a:b:c] -> a <= i < b || step = c
print("\n3 ki tu dau: ", s[0:3])
print("Ki tu 3 tro di: ", s[3:])
print("Step = 2: ", s[::2])
print("Dao nguoc string: ", s[::-1])

a = 'Hello'
b = 'World'

print(a + " " + b)
c = a + b
print("\nPhep cong string: ", c)
print("Nhan string: ", a*3)

print("\nKiem tra ell co trong string a khong: ", "ell" in a)
print("Kiem tra ell co trong string b khong: ", "ell" in b)

print("\nIn hoa: ", s.upper())
print("In thuong: ", s.lower())
print("In hoa 1 chu cai dau: ", s.capitalize())
print("In ten: ", s.title())

name = "    Ho    hoang      QuAN          "
print("\nKi tu mau: ", name)
print("\nXoa khoang trang dau - cuoi: ", name.strip())
print("Replace (hoang -> HOANG): ", name.replace('hoang','HOANG'))
print("Split: ", name.split())
print("Join (Nguoc voi split): ", " ".join(name.split()))

print("\nFind (Tra ve so luong || -1 ): ", name.find('quan'))
print("Count (Dem so luong ki tu): ", name.count('a'))

age = 16
print(f"\nMy name is {name}, I'm {age}")
print("Ep kieu: ", "Age" + str(age))
print("So sanh (Hello) == (World): ", a == b)
print("So sanh (Hello) > (World): ", a > b)
print("So sanh (Hello) < (World): ", a < b)

print("\nKi tu mau: ", s)
print("Startswith - py: ", s.startswith("py"))
print("Endswith - on: ",s.endswith("on"))
print("Is digit: ", s.isdigit())
print("Is alpha: ", s.isalpha())
