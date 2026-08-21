
numbers = [1, 88, 6, 0, 6]

total = 0
average = 0

for i in numbers:
    total += i

average = total/len(numbers)

min = numbers[0]
max = numbers[0]

for i in numbers:
    if min > i: min = i
    if max < i: max = i

print(f"Tong: {total}")
print(f"Trung binh: {average}")
print(f"Lon nhat: {max}")
print(f"Nho nhat: {min}")