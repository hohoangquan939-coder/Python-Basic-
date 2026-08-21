class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} dang keu")


class Dog(Animal): #Ke thua tu class Animal
    pass


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name) # Goi constructor cua Animal
        self.color = color # Day la tham so khong co trong Animal nen phai tu dien lai

    def speak(self):
        print(f"{self.name} {self.color} dang keu meo meo") # Override

