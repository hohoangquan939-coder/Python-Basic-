
def chia_an_toan(a, b):
    try: return int(a)/int(b)
    except ZeroDivisionError: 
            return "Khong the chia cho 0"
    except ValueError:
            return "Du lieu khong hop le"

a = 10
b = 'a'
print(f"{a} / {b} = {chia_an_toan(a, b)}")