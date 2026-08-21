def dao_nguoc(lst):
    i = 0
    j = len(lst)-1

    while(i <= j):
        tmp = lst[i]
        lst[i] = lst[j]
        lst[j] = tmp
        i+=1; j-=1


a = list(map(int, input("Nhap day so: ").split()))

dao_nguoc(a)
print(a)
print(a[::-1])
a.reverse()
print(a)





