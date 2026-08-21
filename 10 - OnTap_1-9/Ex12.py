def la_doi_xung(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
s = input("Nhap chuoi: ")
print(f"Chuoi doi xung: {la_doi_xung(s)}") 