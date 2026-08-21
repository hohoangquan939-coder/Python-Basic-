class Animal:
    def speak(self):
        print(f"haha")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

Lst = [Cat(), "Nhi", Dog(), "Quan"]

for i in Lst:
    if isinstance(i, Animal):
        i.speak()
    else: print("Day khong phai Animal")