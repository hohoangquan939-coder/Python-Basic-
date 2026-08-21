#Dictionary trong Python giong voi Map trong C++

student = {
    "name": "Quan",
    "age": 20,
    "score": 8.5
}

print(student["name"])
print(student["age"])

student["email"] = "quan@gmail.com" #them
student["age"] += 1                 #sua
del student["score"]                #xoa

print(student)


#Duyet dict
for key in student:
    print(key, ":", student[key])

for key, value in student.items():
    print(key, ":", value)

if "name" in student:
    print("Co key name")

#Dung get de truy cap neu khong chac key co hay khong
print(student.get("phone"))         #tra ve none
print(student.get("phone", "N/A"))  #tra ve "N/A"


#EXERCISE

product = {
    "name": "quan",
    "price": 50,
    "stock": 18
}

print(product["name"])
print(product["price"])

product["price"] *= 0.9
product["category"] = 9

del product["stock"]

print(product.get("discount", "Khong co khuyen mai"))


for key in product:
    print(key, " : ", product[key])