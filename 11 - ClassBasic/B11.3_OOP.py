class Student:

    def __init__(self, name, math, physics, english):
        self.name = name
        self.math = math
        self.physics = physics
        self.english = english

    def average(self):
        return round((self.math + self.english + self.physics)/3, 2)
    
    def rank(self):
        ave = self.average()
        if ave >= 8: return 'Gioi'
        elif ave >= 6.5: return 'Kha'
        elif ave >= 5: return 'Trung binh'
        else: return 'Yeu'

    def show(self):
        print(f"Ten: {self.name}")
        print(f"Toan: {self.math} - Ly: {self.physics} - Anh: {self.english}")
        print(f"Diem trung binh: {self.average()} - Xep loai: {self.rank()}")



sv1 = Student("Quan", 9.5, 9.5, 8)
sv1.show()