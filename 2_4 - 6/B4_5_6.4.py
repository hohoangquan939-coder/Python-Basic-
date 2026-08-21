
numbers = [1,2,3,4,5,6,7,8,9,0]

# Ham show - Co the dung print de in toan bo list
def show(lst):
    for i in lst:
        print(i, end = ' ')
    print("")

#  Ham loc cac so chan trong 1 list
def loc_chan(lst):
    chan = []
    for i in lst:
        if i%2 == 0: chan.append(i)

    return chan

# Ham loc cac so le trong 1 list
def loc_le(lst):
    le = []
    for i in lst:
        if (i%2 != 0): le.append(i)

    return le

# Ham loc so lon hon n
def lon_hon_n(lst, n):
    lonhon = []
    for i in lst:
        if i > n: lonhon.append(i)
    return lonhon


print("Numbers: ", end = "")
print(numbers)
n = int(input("Nhap so n lam moc: "))


chan = loc_chan(numbers)
le = loc_le(numbers)
lon = lon_hon_n(numbers, n)

print("Cac so lon hon n trong list numbers: ", end = "")
show(lon)
print("Cac so chan trong list numbers: ", end = "")
show(chan)
print("Cac so le trong list numbers: ", end = "")
show(le)

