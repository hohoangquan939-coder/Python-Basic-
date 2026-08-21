def loc_so_chan(lst):
    lst_res = []
    for x in lst:
        if x%2 == 0:
            lst_res.append(x)
    return lst_res


def loc_so_chan_1(lst):
    for x in lst[:]:
        if x%2!=0:
            lst.remove(x)
    return lst


def dem_ky_tu(s):
    dic = {}
    for x in s:
        if x != ' ':
            if x not in dic:
                dic[x] = 1
            else:
                dic[x] += 1
    return dic


def dao_nguoc(s):
    lst = s.split()
    return " ".join(lst[::-1])


def tinh_giai_thua(n):
    if n == 1 or n == 0:  return 1
    return n*tinh_giai_thua(n-1)

def tim_2_so_lon_nhat(mang):
    if len(mang) == 1:
        return (mang[0], mang[0])

    if mang[0] >= mang[1]:
        m1 = mang[0] # Lon nhat
        m2 = mang[1] # Lon nhi
    else:
        m1 = mang[1]
        m2 = mang[0]

    for i in range(2, len(mang)):
        x = mang[i]
        if x>m2:
            if x>m1: 
                m2 = m1
                m1 = x
            else:
                m2 = x
    return (m1, m2)


t = tim_2_so_lon_nhat([1,2,3,4,55,6,99, 7,88,99])
print(t)
