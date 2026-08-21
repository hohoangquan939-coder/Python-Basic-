def tim_max(lst):
    vt_max = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[vt_max]: vt_max = i
    return vt_max, lst[vt_max]


numbers = [12, 45, 7, 89, 23, 56, 3]
k, a = tim_max(numbers)

print(f"Gia tri lon nhat: {a}")
print(f"Vi tri: {k}")
