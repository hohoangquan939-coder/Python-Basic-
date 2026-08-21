def dem_tu_trong_dong(s):
    return len(s.split())

def main():
    with open("data.txt", "r") as f:
        dong, tu = 0, 0
        dong_max = ""
        for line in f:
            line = line.strip()
            dong += 1
            tu += dem_tu_trong_dong(line)
            if len(dong_max) < len(line): dong_max = line

    print(f"So dong: {dong}")
    print(f"Tong so tu: {tu}")
    print(f"Dong dai nhat: {dong_max}")

main()