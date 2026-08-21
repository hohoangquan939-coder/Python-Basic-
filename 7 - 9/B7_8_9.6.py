


name = input("Nhap ten: ")

while True:
    try:
        score = float(input("Nhap diem: "))

        
    except ValueError:
        print("Diem phai nhap so!")
        continue
    if score<0 or score>10:
        print("Diem phai tu 0 den 10!")
        continue

    print(f"Ten: {name} - Diem: {score}")
    break
