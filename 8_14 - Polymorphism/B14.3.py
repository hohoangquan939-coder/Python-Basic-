from abc import ABC, abstractmethod

#ABC: class dac biet

class Animal(ABC): # ke thua tu ABC class - Khong duoc phep tao Object truc tiep tu Animal
    @abstractmethod # Decorator
    def speak(self):
        print("Hello")


class Dog(Animal):

    def speak(self):
        print(f"Gau Gau")

class Cat(Animal):
    def speak(self):
        print(f"Meo meo")


b = Cat()
c = Dog()