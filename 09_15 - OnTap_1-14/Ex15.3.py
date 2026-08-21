from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, id):
        self.name = name
        self.__id = id
    
    @abstractmethod
    def vai_tro(self):
        pass

    def get_id(self):
        return self.__id

class Student(Person):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.__scores = {}

    def get_scores(self):
        return self.__scores

    def vai_tro(self):
        return "Hoc sinh"
    
    def them_diem(self, mon, diem):
        self.__scores[mon] = diem
    
    def diem_trung_binh(self):
        average_score = 0
        if not self.__scores: return 0
        for diem in self.__scores.values():
            average_score += diem
        # return sum(self.__scores.values()) / len(self.__scores)
        return average_score / len(self.__scores)
    
    def xep_loai(self):
        if not self.__scores: return 'Khong xep hang'

        average_score = self.diem_trung_binh()
        if average_score >= 9: return 'Xuat sac'
        elif average_score >= 8: return 'Gioi'
        elif average_score >= 6: return 'Kha'
        elif average_score >= 5: return 'Trung binh'
        else: return 'Yeu'

    def thong_tin(self):
        print(f"Ten: {self.name:<15} - Vai tro: {self.vai_tro():<15} - Id: {self.get_id():<15}")

    def bang_diem(self):
        print(f"Bang diem cua sinh vien: {self.name} ")
        if not self.__scores: print(f"Khong co mon hoc nao")
        else:
            for mon, diem in self.__scores.items():
                print(f"Mon: {mon} - Diem: {diem}")
        print(f"Diem trung binh: {self.diem_trung_binh()}")
        print(f"Xep hang: {self.xep_loai()}")
        

class Teacher(Person):
    def __init__(self, name, id, subject):
        super().__init__(name, id)
        self.subject = subject
        self.__students = []

    def vai_tro(self):
        return "Giao vien"
    
    def them_hoc_sinh_phu_trach(self, student):
        self.__students.append(student)

    def diem_trung_binh_lop(self):
        average_class = 0
        if not self.__students: return 0
        for student in self.__students:
            average_class += student.diem_trung_binh()
        return average_class/len(self.__students)
    
    def thong_tin(self):
        print(f"Ten: {self.name:<15} - Vai tro: {self.vai_tro():<15} - Id: {self.get_id():<15}")
        print(f"Mon phu trach: {self.subject}")
        print(f"Danh sach hoc sinh phu trach: ")
        if not self.__students: print(f"Chua co hoc sinh phu trach")
        else:
            for student in self.__students:
                student.thong_tin()

class School:
    def __init__(self, name):
        self.name = name
        self.__people = []
    
    def them_nguoi(self, person):
        self.__people.append(person)

    def liet_ke_theo_vai_tro(self, vaitro):
        lst = []
        for person in self.__people:
            if person.vai_tro() == vaitro: lst.append(person)
        return lst

    def hoc_sinh_gioi_nhat(self):
        best_student = None
        for person in self.__people:
            if isinstance(person, Student):
                if best_student == None:
                    best_student = person
                elif best_student.diem_trung_binh() < person.diem_trung_binh(): 
                    best_student = person
        return best_student
    
    def xuat_bao_cao(self, filename):
        lst_giao_vien = self.liet_ke_theo_vai_tro('Giao vien')
        lst_hoc_sinh = self.liet_ke_theo_vai_tro('Hoc sinh')
        with open(filename, 'w') as f:
            if lst_giao_vien:
                f.write(f"Giao vien\n")
            for person in lst_giao_vien:
                f.write(f"Ten: {person.name} - Id: {person.get_id()}\n")

            if lst_hoc_sinh:
                f.write(f"Hoc sinh\n")
            for person in lst_hoc_sinh:
                f.write(f"Ten: {person.name} - Id: {person.get_id()}\n")

    def doc_bao_cao(self, filename):
        try:
            with open(filename, 'r') as f:
                for line in f:
                    print(line.strip())

        except FileNotFoundError:
                print(f"Khong tim thay file")

def test_co_san():
    dics_diem = {
        'Toan': 8,
        'Hoa': 6,
        'Ly': 7 
       }
    
    sv1 = Student('Quan', '109008798023')
    sv2 = Student('Nhi', '139008798023')
    sv3 = Student('Hung', '129008798023')
    sv4 = Student('Quang', '119008798023')

    lst_students = [sv1, sv2, sv3, sv4]

    for mon, diem in dics_diem.items():
        for student in lst_students:
            student.them_diem(mon, diem)

    gv1 = Teacher('Thuy', '10998903', 'Toan')

    for student in lst_students:
        gv1.them_hoc_sinh_phu_trach(student)
    
    lst_people = [sv1, sv2, sv3, sv4, gv1]

    sc = School('THPT QUE SON')
    for people in lst_people:
        sc.them_nguoi(people)
    
    sc.xuat_bao_cao('EX15_3.txt')
    sc.doc_bao_cao('EX15_3.txt')

def nhap_so_nguyen(a, b):
    while True:
        x = input("")
        try:
            x = int(x)
            if x < a or x > b: 
                print(f"Loi! Vui long nhap lai: ", end = "")
                continue
            return x
        except ValueError:
            print(f"Loi! Vui long nhap lai: ", end = "")

# chi duoc nhap trong [a, b]
def nhap_so_thuc(a, b):
    while True:
        x = input("")
        try:
            x = float(x)
            if x < a or x > b: 
                print(f"Loi! Vui long nhap lai: ", end = "")
                continue
            return x
        except ValueError:
            print(f"Loi! Vui long nhap lai: ", end = "")


# Tu nhap bang tay
def test_tu_nhap():
    name_school = input(f"Nhap ten cua truong: ")
    school1 = School(name_school)

    lst_giao_vien = []
    lst_hoc_sinh = []

    while True:
        role = input(f"\nNhap vai tro muon them (giao vien / hoc sinh / end): ")

        if role == 'giao vien':
            name_teacher = input(f"\nNhap ten giao vien: ")
            id_teacher = input(f"Nhap id cua giao vien: ")
            subject = input(f"Nhap mon hoc phu trach (Toan / Li / Hoa): ")
            while subject not in ['Toan', 'Li', 'Hoa']:
                subject = input(f"Loi! Vui long nhap lai mon hoc (Toan / Li / Hoa): ")
            
            gv = Teacher(name_teacher, id_teacher, subject)
            lst_giao_vien.append(gv)

        elif role == 'hoc sinh':
            name_student = input(f"\nNhap ten hoc sinh: ")
            id_student = input(f"Nhap id cua hoc sinh: ")
            sv = Student(name_student, id_student)
            number_subject = 0
            while True:
                if number_subject >= 2:
                    print(f"Hoc sinh nay da du 2 mon. Ban co muon them mon khong?")
                    print(f"1. Co - 0. Khong")
                    print(f"Nhap lua chon cua ban: ", end = "")
                    lua_chon = nhap_so_nguyen(0, 1)
                    if lua_chon == 0: break

                while True:
                    subject = input("Nhap mon hoc dang ki (Toan / Li / Hoa): ")

                    if subject not in ["Toan", "Li", "Hoa"]:
                        print("Mon hoc khong hop le!")
                    elif subject in sv.get_scores():
                        print("Hoc sinh da dang ki mon hoc nay!")
                    else:
                        break

                number_subject += 1
                print(f"Nhap diem mon {subject}: ", end = "")
                score = nhap_so_thuc(0, 10)
                sv.them_diem(subject, score)

            lst_hoc_sinh.append(sv)

        elif role == 'end':
            break
        else:
            print(f"Loi! Vui long nhap lai")

    # Them tung nguoi vao truong
    for person in lst_giao_vien:
        school1.them_nguoi(person)
    for person in lst_hoc_sinh:
        school1.them_nguoi(person)

    # Tu dong them hoc sinh ma giao vien phu trach
    for gv in lst_giao_vien:
        for sv in lst_hoc_sinh:
            if gv.subject in sv.get_scores():
                gv.them_hoc_sinh_phu_trach(sv)

    print(f"\nNhung thong tin ban da nhap")
    print(f"\nGiao vien")
    if lst_giao_vien:
        for person in lst_giao_vien:
            person.thong_tin()
            print(f"")

    print(f"\nHoc sinh")
    if lst_hoc_sinh:
        for person in lst_hoc_sinh:
            person.thong_tin()

    print(f"\nBao cao: ")

    sv = school1.hoc_sinh_gioi_nhat() 
    print(f"\nHoc sinh gioi nhat: ")
    if sv:
        sv.thong_tin()
    else:
        print(f"Chua co sinh vien nao")
        
    print(f"\nDiem trung binh tung lop theo giao vien: \n")
    for mon in ['Toan', 'Li', 'Hoa']:
        print(f"Lop {mon}")
        for person in lst_giao_vien:
            if person.subject == mon:
                print(f"Giao vien: {person.name} - Diem trung binh lop: {person.diem_trung_binh_lop()}")
        print(f"")
        
    school1.xuat_bao_cao('EX15_3.txt')

test_tu_nhap()