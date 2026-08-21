from abc import ABC, abstractmethod

class Media(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_borrowed = False
    
    @abstractmethod
    def thoi_gian_muon_toi_da(self):
        pass # return int

    @abstractmethod
    def phi_tre_han(self, days_late):
        pass # return int (so tien phat)

    @abstractmethod
    def loai(self):
        pass 

    def muon(self):
        if self._is_borrowed == True:
            raise Exception(f"{self.title} dang duoc muon")
        else:
            self._is_borrowed = True
    
    def tra(self):
        self._is_borrowed = False
    
    def dang_duoc_muon(self):
        return self._is_borrowed

    def thong_tin(self):
        return (f"{self.title:<20} | {self.author:<20} | {'Dang muon' if self._is_borrowed else 'Con trong':<10}")
    

class Book(Media):
    def __init__(self, title, author, num_pages):
        super().__init__(title, author)
        self.num_pages = num_pages
    
    def thoi_gian_muon_toi_da(self):
        return 14
    
    def phi_tre_han(self, days_late):
        return days_late * 2000
    
    def loai(self):
        return 'Sach'

class DVD(Media):
    def __init__(self, title, author, duration_minutes):
        super().__init__(title, author)
        self.duration_minutes = duration_minutes
    
    def thoi_gian_muon_toi_da(self):
        return 3
    
    def phi_tre_han(self, days_late):
        return days_late * 10000

    def loai(self):
        return 'DVD'
    

class Magazine(Media):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.issue_number = issue_number
    
    def thoi_gian_muon_toi_da(self):
        return 7
    
    def phi_tre_han(self, days_late):
        return days_late * 5000

    def loai(self):
        return 'Tap chi'


class Member:
    def __init__(self, name):
        self.name = name
        self._borrowed_list = []
    
    def muon_media(self, media):
        try:
            media.muon()
            self._borrowed_list.append(media)
            print(f"{self.name} da muon: {media.title}")
        except Exception as e:
            print(e)
    
    def tra_media(self, media):
        if media in self._borrowed_list:
            media.tra()
            self._borrowed_list.remove(media)
            print(f"{self.name} da tra: {media.title}")
        else:
            print(f"{self.name} khong co muon {media.title}")
    

    def tinh_tong_phi_tre_han(self, days_late_dict):
        total = 0
        for key, value in days_late_dict.items():
            total += key.phi_tre_han(value)
        
        return total

    def thong_tin(self):
        print(f"Ten: {self.name} ")
        print(f"Danh sach cac media dang muon")
        for item in self._borrowed_list:
            print(f"{item.title}")
    

class Library:
    def __init__(self, name):
        self.name = name
        self._catalog = []
        self._member = []
    
    def them_media(self, media):
        self._catalog.append(media)
    
    def them_thanh_vien(self, member):
        self._member.append(member)
    
    def tim_media_con_trong(self):
        lst_media = []
        for item in self._catalog:
            if item.dang_duoc_muon() is False:
                lst_media.append(item)
        return lst_media

    def lst_book_con_lai(self):
        lst_book = []
        for item in self._catalog:
            if item.loai() == 'Sach' and not item.dang_duoc_muon():
                lst_book.append(item)
        return lst_book
    
    def lst_DVD_con_lai(self):
        lst_DVD = []
        for item in self._catalog:
            if item.loai() == 'DVD' and not item.dang_duoc_muon():
                lst_DVD.append(item)
        return lst_DVD

    def lst_magazine_con_lai(self):
        lst_magazine = []
        for item in self._catalog:
            if item.loai() == 'Tap chi' and not item.dang_duoc_muon():
                lst_magazine.append(item)
        return lst_magazine

    def thong_ke_theo_loai(self):
        count_book = 0
        count_dvd = 0
        count_magazine = 0
        for item in self._catalog:
            if item.loai() == 'Sach': 
                count_book += 1
            elif item.loai() == 'DVD':
                count_dvd += 1
            else:
                count_magazine += 1
        dict_count = {}
        dict_count['Book'] = count_book
        dict_count['DVD'] = count_dvd
        dict_count['Magazine'] = count_magazine
        return dict_count
    
    def xuat_bao_cao(self, filename):
        lst_book = self.lst_book_con_lai()
        lst_dvd = self.lst_DVD_con_lai()
        lst_magazine = self.lst_magazine_con_lai()
        with open(filename, 'w') as f:
            f.write(f"Thu vien: {self.name}\n")
            f.write(f"====================================================================\n")
            f.write(f"SACH ({len(lst_book)})\n")
            for item in lst_book:
                f.write(f"- {item.thong_tin()}\n")

            f.write(f"====================================================================\n")
            f.write(f"DVD ({len(lst_dvd)})\n")
            for item in lst_dvd:
                f.write(f"- {item.thong_tin()}\n")
            
            f.write(f"====================================================================\n")
            f.write(f"TAP CHI ({len(lst_magazine)})\n")
            for item in lst_magazine:
                f.write(f"- {item.thong_tin()}\n")

    def doc_bao_cao(self, filename):
        try:
            with open(filename, 'r') as f:
                for line in f:
                    print(line.strip())
        except FileNotFoundError:
            print(f"Loi! Khong tim thay file")



def main():
    lib = Library("Thu Vien Trung Tam")

    # Tao media
    b1 = Book("Harry Potter", "J.K Rowling", 500)
    b2 = Book("Dac Nhan Tam", "Dale Carnegie", 320)
    b3 = Book("Clean Code", "Robert Martin", 431)
    d1 = DVD("Avengers", "Marvel", 180)
    d2 = DVD("Interstellar", "Nolan", 169)
    m1 = Magazine("Forbes", "Forbes Inc", 102)
    m2 = Magazine("National Geographic", "Nat Geo", 55)

    for media in [b1, b2, b3, d1, d2, m1, m2]:
        lib.them_media(media)

    # Tao thanh vien
    mem1 = Member("Quan")
    mem2 = Member("Nhi")
    mem3 = Member("Hung")

    for mem in [mem1, mem2, mem3]:
        lib.them_thanh_vien(mem)

    # Test muon/tra
    mem1.muon_media(b1)
    mem1.muon_media(d1)
    mem2.muon_media(b1)   # ← lỗi: b1 đang được mượn bởi mem1
    mem2.muon_media(m1)
    mem2.muon_media(m1)   # ← test Magazine borrow_count

    mem1.tra_media(b1)
    mem2.muon_media(b1)   # ← giờ mượn được vì mem1 đã trả

    # Test phi tre han
    ngay_tre = {d1: 2, b1: 0}
    phi = mem1.tinh_tong_phi_tre_han(ngay_tre)
    print(f"\nPhi tre han cua {mem1.name}: {phi} VND")

    # Thong ke
    print(f"\nThong ke theo loai: {lib.thong_ke_theo_loai()}")
    print(f"\nMedia con trong:")
    for media in lib.tim_media_con_trong():
        print(f"{media.thong_tin()}")

    # Xuat bao cao
    lib.xuat_bao_cao("EX15_7.txt")
    lib.doc_bao_cao("EX15_7.txt")



main()