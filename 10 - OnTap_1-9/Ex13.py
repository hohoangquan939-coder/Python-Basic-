
def ma_hoa(s, k):
    res = ""
    for c in s:
        if c == " ":
            res += " "
        else:
            res += chr((ord(c) - ord('a') + k) % 26 + ord('a'))
    return res

s = input("Nhap chuoi: ")
k = int(input("Nhap k: "))

print(f"Chuoi ma hoa: {ma_hoa(s, k)}")