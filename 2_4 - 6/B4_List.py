fruits = ["apple", "banana", "orange"]

mixed  = [1, "hello", True, 3.14]

print(fruits[0])
print(fruits[-1])
print(len(fruits))

fruits.append("grape")
fruits.insert(1, "mango")
fruits.remove("banana")
fruits.pop() #xoa grape

print(fruits)

for fruit in fruits:
    print(fruit)

numbers = [1, 2, 3, 4, 5]
print(numbers[1:4]) #1, 2, 3
print(numbers[:3])
print(numbers[3:])
print(numbers[::2]) #buoc nhay 2

students = ["An", "Binh", "Vu", "Mai", "Huong"]
print(students[0])
print(students[4])
students.append("Quan")
students.remove(students[2])


for i in range (len(students)):
    print(f"{i+1}. {students[i]}")
