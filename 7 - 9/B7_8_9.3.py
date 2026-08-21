
name = input("Nhap ho ten: ")

res = " ".join(name.title().split())


print(f"Ho ten chuan: {res}")
print(f"So ky tu(khong tinh khoang trang): {len(res) - res.count(' ')}")
print(f"Co chu Hoang: {'Hoang' in res}")