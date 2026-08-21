from abc import ABC, abstractmethod
import random
import os
import copy

class Character(ABC):
    def __init__(self, name, max_hp, atk, max_mana):
        self.name = name
        self._hp = max_hp
        self._max_hp = max_hp
        self.atk = atk
        self.cur_mana = max_mana
        self.max_mana = max_mana

    @abstractmethod
    def dung_ki_nang(self, targets):
        pass

    @abstractmethod
    def chuc_vu(self):
        pass

    def tang_mana(self):
        if self.cur_mana < self.max_mana:
            self.cur_mana += 1

    def kiem_tra_day_mana(self):
        if self.cur_mana == self.max_mana:
            return True
        else:
            return False

    def con_song(self):
        if self._hp > 0:
            return True
        else:
            return False

    def nhan_st(self, amount):
        if self._hp - amount <= 0:
            self._hp = 0
        else:
            self._hp = round(self._hp - amount, 2)

    def tan_cong(self, target):
        print(f"{self.name} ({self.chuc_vu()}) tan cong: {target.name} ({target.chuc_vu()}) ({self.atk}st)")
        target.nhan_st(self.atk)

    def hoi_mau(self, amount):
        if self._hp + amount >= self._max_hp:
            self._hp = self._max_hp
        else:
            self._hp += amount

    def get_hp(self):
        return self._hp

    def get_max_hp(self):
        return self._max_hp

    def thong_tin(self):
        print(f"{self.name:<30} | {self.chuc_vu():<25} | {self._hp:>6}/{self._max_hp:>4} | ATK: {self.atk:<5} | Mn: {self.cur_mana}/{self.max_mana}")

class Warrior(Character):
    def __init__(self, name,  max_hp = 170, atk = 34):
        super().__init__(name, max_hp, atk, 3)

    # x2 damage len muc tieu
    def dung_ki_nang(self, target):
        self.cur_mana = 0
        target.nhan_st(self.atk * 2)
        print(f"[*] {self.name} ({self.chuc_vu()}) da dung ki nang tang sat thuong len: {target.name} ({target.chuc_vu()}) ({self.atk*2}st (x2 sat thuong))")

    def tang_mana(self):
        if self.cur_mana < self.max_mana:
            self.cur_mana += 1

    def chuc_vu(self):
        return 'Chien binh'


class Tanker(Character):
    def __init__(self, name, max_hp = 500, atk = 15 ):
        super().__init__(name, max_hp, atk, 4)

    # Khieu khich quai va tang giap ao
    def dung_ki_nang(self, target = None):
        self.cur_mana = 0
        self.hoi_mau(50)
        print(f"[*] {self.name} ({self.chuc_vu()}) da dung ki nang khieu khich toan bo ac ma")
        # Can cho toan bo quai tan cong Tanker nay

    def tang_mana(self):
        if self.cur_mana < self.max_mana:
            self.cur_mana += 1

    def chuc_vu(self):
        return 'Do don'


class Healer(Character):
    def __init__(self, name, max_hp = 200, atk = 5 ):
        super().__init__(name, max_hp, atk, 3)

    def dung_ki_nang(self, target):
        self.cur_mana = 0
        target.hoi_mau(140)
        print(f"[*] {self.name} ({self.chuc_vu()}) da dung ki nang hoi mau (+40 hp) cho: {target.name} ({target.chuc_vu()})")

    def tang_mana(self):
        if self.cur_mana < self.max_mana:
            self.cur_mana += 1

    def chuc_vu(self):
        return 'Thay thuoc'

class Mage(Character):
    def __init__(self, name, max_hp = 180, atk = 35):
        super().__init__(name, max_hp, atk, 4)

    def dung_ki_nang(self, target):
        self.cur_mana = 0
        for char in target:
            char.nhan_st(20)
        print(f"[*] {self.name} ({self.chuc_vu()}) da dung ki nang tan cong dien rong vao toan bo ke dich (20st)")

    def chuc_vu(self):
        return 'Phap su'


class Priest(Character):
    def __init__(self, name, max_hp = 140, atk = 25):
        super().__init__(name, max_hp, atk, 6)

    def dung_ki_nang(self, target):
        self.cur_mana = 0
        target.cur_mana = target.max_mana 
        print(f"[*] {self.name} ({self.chuc_vu()}) da dung ki nang hoi skill ngay lap tuc cho: {target.name} ({target.chuc_vu()})")

    def chuc_vu(self):
        return 'Tu te'


class Assassin(Character):
    def __init__(self, name, max_hp = 140, atk = 30 ):
        super().__init__(name, max_hp, atk, 5)

    def dung_ki_nang(self, target):
        self.cur_mana = 0
        percent = target.get_hp() / target.get_max_hp()
        if percent <= 0.3:
            damage = 100
        elif percent <= 0.6:
            damage = 60
        else:
            damage = 40
        target.nhan_st(damage)
        print(f"[*] {self.name} ({self.chuc_vu()}) da dung ki nang am sat vao: {target.name} ({target.chuc_vu()}) ({damage}st)")

    def chuc_vu(self):
        return 'Sat thu'


class PoisonMaster(Character):
    def __init__(self, name, max_hp = 200, atk = 13):
        super().__init__(name, max_hp, atk, 3)
        self._lst_target = []

    # Them 1 ke thu vao list bi dinh doc
    def dung_ki_nang(self, target):
        self.cur_mana = 0
        self._lst_target.append(target)
        print(f"[*] {self.name} ({self.chuc_vu()}) da tam doc vao: {target.name} ({target.chuc_vu()})")

    def tan_cong(self, target):
        new_lst_target = []

        for char in self._lst_target:
            char.nhan_st(self.atk)
            print(f"[*] {self.name} ({self.chuc_vu()}) tan cong ke bi tam doc: {target.name} ({target.chuc_vu()}) ({self.atk}st)")
            if char.con_song():
                new_lst_target.append(char)
        self._lst_target = new_lst_target
        target.nhan_st(self.atk)
        print(f"{self.name} ({self.chuc_vu()}) tan cong: {target.name} ({target.chuc_vu()}) ({self.atk}st)")

    def chuc_vu(self):
        return 'Doc thu'


class LifeStealer(Character):
    def __init__(self, name, max_hp = 200, atk = 27):
        super().__init__(name, max_hp, atk, 5)

    def dung_ki_nang(self, target):
        self.cur_mana = 0
        dame = round(target.get_hp() * 0.4, 2)
        if dame > 300:
            dame = 300
        # Gay sat thuong vao ke dich
        target.nhan_st(dame)
        # Hoi mau cho ban than
        self.hoi_mau(dame * 0.5)
        print(f"[*] {self.name} ({self.chuc_vu()}) da hut mau ke dich: {target.name} ({target.chuc_vu()}) ({dame}st)")

    def chuc_vu(self):
        return 'Ma ca rong'


class DarkKnight(Character):
    def __init__(self, name, max_hp = 230, atk = 44):
        super().__init__(name, max_hp, atk, 0)
        self.max_mn1_steal = 4  # Giam 5%HP hien tai va + 30%ATK vao doi thu duoc chon trong turn danh
        self.max_mn2_mark = 3   # Giam 10%HP hien tai + danh dau doi thu, neu sau 2 luot muc tieu chet thi: +30%HP va +10ATK truc tiep
        self.cur_mn1_steal = 4
        self.cur_mn2_mark = 3
        self.marked_enemy = None
        self.time_marked_enemy = -1

    def kiem_tra_day_mana(self):
        return self.cur_mn1_steal == self.max_mn1_steal or self.cur_mn2_mark == self.max_mn2_mark

    def dung_ki_nang(self, target):
        select = 0
        if self.cur_mn1_steal < self.max_mn1_steal:
            select = 2
        elif self.cur_mn2_mark < self.max_mn2_mark:
            select = 1
        else:
            print(f'Ki nang cua Dark Knight: 1. Ki nang hien te - 2. Danh dau muc tieu')
            select = int(input(f'Nhap 1 hoac 2 de lua chon: '))

        if select == 1:
            self.cur_mn1_steal = 0
            self.nhan_st(self.get_hp() * 0.05)
            target.nhan_st(self.atk * (1 + 0.3))
            print(f"[*] {self.name} ({self.chuc_vu()}) da dung ki nang hien te mau va tan cong ke dich: {target.name} ({target.chuc_vu()}) ({round(self.atk*1.3, 2)}st)")

        else:
            self.cur_mn2_mark = 0
            self.nhan_st(self.get_hp() * 0.1)
            self.marked_enemy = target
            self.time_marked_enemy = -1
            print(f"[*] {self.name} ({self.chuc_vu()}) da dung ki nang danh dau vao ke dich: {target.name} ({target.chuc_vu()})")

    def tang_mana(self):
        if self.cur_mn1_steal < self.max_mn1_steal:
            self.cur_mn1_steal += 1
        if self.cur_mn2_mark < self.max_mn2_mark:
            self.cur_mn2_mark += 1

    def check_marked_enemy(self):
        if self.marked_enemy is None:
            return

        self.time_marked_enemy += 1

        if self.marked_enemy.con_song():
            if self.time_marked_enemy >= 2:
                self.marked_enemy = None
                self.time_marked_enemy = -1

        else:
            if self.time_marked_enemy < 2:
                self.hoi_mau(self.get_max_hp() * 0.3)
                self.atk += 6

            self.marked_enemy = None
            self.time_marked_enemy = -1
                
    def chuc_vu(self):
        return 'Hiep si bong dem'
    
    def thong_tin(self):
        print(f"{self.name:<30} | {self.chuc_vu():<25} | {self._hp:>6}/{self._max_hp:>4} | ATK: {self.atk:<5} | Mn1: {self.cur_mn1_steal}/{self.max_mn1_steal} - Mn2: {self.cur_mn2_mark}/{self.max_mn2_mark}", f"- ({self.marked_enemy.name}: TL: {2-self.time_marked_enemy})" if self.marked_enemy else "")



class Orc(Character):
    def __init__(self, name, size, max_hp = 50, atk = 27):
        self.size = size
        if self.size == 1:
            super().__init__(name, max_hp, atk, 3)
            self.slot = 1
        elif self.size == 2:
            super().__init__(name, max_hp + 50, atk + 4, 3)
            self.slot = 2
        else:
            super().__init__(name, max_hp + 100, atk + 8, 3)
            self.slot = 3

    def dung_ki_nang(self, target):
        self.cur_mana = 0
        target.nhan_st(self.atk * 1.2)
        print(f"[*] {self.name} ({self.chuc_vu()}) da dung ki nang danh ke dich: {target.name} ({target.chuc_vu()}) ({self.atk*1.2}st)")

    def chuc_vu(self):
        if self.size == 1:
            return 'Orc nho'
        elif self.size == 2:
            return 'Orc thuong'
        else:
            return 'Orc khong lo'


class Golem(Character):
    def __init__(self, name, type ,max_hp = 700, atk = 13):
        self.type = type # 1.thuong - 2.Phu thuy
        if self.type == 1:
            super().__init__(name, max_hp, atk, 6)
            self.slot = 8
        else:
            super().__init__(name, max_hp+100, atk+4, 6)
            self.slot = 12

    def dung_ki_nang(self, target):
        self.cur_mana = 0
        self.hoi_mau(200)
        if self.type == 2:
            if target.atk > 2:
                target.atk -= 3
        print(f"[*] {self.name} ({self.chuc_vu()}) da dung ki nang hoi mau (100hp)", f"va khien {target.name} ({target.chuc_vu()}) mat 3atk" if self.type == 2 else f"")

    def chuc_vu(self):
        if self.type == 2:
            return 'Golem Phu Thuy'
        else:
            return 'Golem'


class GoblinAcher(Character):
    def __init__(self, name, type ,max_hp = 70, atk = 24):
        super().__init__(name, max_hp, atk, 3)
        self.slot = 3
        self.type = type # 1: thuong khong co ki nang- 2: bang lam giam sat thuong cua dich - 3: lua tang sat thuong
        # ki nang dac biet: sat thuong chi mang x 2,3

    def dung_ki_nang(self, target):
        self.cur_mana = 0
        critic = random.random()
        cur_damage = self.atk
        if critic <= 0.3:
            cur_damage *=  2.3
            print(f"[*] {self.name} ({self.chuc_vu()}) da dung ki nang va dat chi mang (x2.3) st")
        if self.type == 2:
            target.atk -=3
        elif self.type == 3:
            cur_damage *= 1.2
        cur_damage = round(cur_damage, 2)
        target.nhan_st(cur_damage)
        print(f"[*] {self.name} ({self.chuc_vu()}) da dung ki nang cung thu vao ke dich: {target.name} ({target.chuc_vu()}) ({cur_damage}st)", f"va khien muc tieu -3atk" if self.type==2 else f"")

    def chuc_vu(self):
        if self.type == 1:
            return 'Ma Xa'
        elif self.type == 2:
            return 'Bang Ma Xa'
        else:
            return 'Hoa Ma xa'


class ShadowAssassin(Character):
    def __init__(self, name ,max_hp = 60, atk = 14):
        super().__init__(name, max_hp, atk, 2)
        self.slot = 6

    def dung_ki_nang(self, target):
        self.cur_mana = 0
        critic = random.random()
        ratio = target.get_hp() / target.get_max_hp()
        damage = self.atk

        if ratio >= 0.7:
            damage *= 1.2
        elif ratio >= 0.4:
            damage *= 1.4
        elif ratio >= 0.2:
            damage *= 1.6
        else:
            damage *= 1.8

        if critic <= 0.8:
            damage *= 1.7
        damage = round(damage,2)
        target.nhan_st(damage)
        print(f"[*] {self.name} ({self.chuc_vu()}) da dung ki nang am sat vao: {target.name} ({target.chuc_vu()}) ({damage}st)")

    def chuc_vu(self):
        return 'Sat thu bong dem'

# Single Target
class Zombie(Character):
    def __init__(self, name, type ,max_hp = 20, atk = 18):
        super().__init__(name, max_hp, atk, 2)
        self.type = type # 1, 2, 3, 4
        if self.type == 1:
            self.slot = 1
        elif self.type == 2:
            self.slot = 2
        else:
            self.slot = 4

        self.marked_enemy = None

    def dung_ki_nang(self, target):
        self.cur_mana = 0
        if self.type == 1:
            target.nhan_st(self.atk) # Tan cong thuong
            print(f"[*] {self.name} ({self.chuc_vu()}) da dung ki nang danh ke dich: {target.name} ({target.chuc_vu()}) ({self.atk}st)")

        elif self.type == 2:
            target.nhan_st(self.atk * 1.1)
            self.hoi_mau(4) # Tan cong va hoi mau
            print(f"[*] {self.name} ({self.chuc_vu()}) da dung ki nang danh ke dich: {target.name} ({target.chuc_vu()}) ({self.atk*1.1}st) va hoi 4hp")

        elif self.type == 3:
            dame = round(self.atk * 1.2, 2)
            target.nhan_st(dame)
            reduce_atk = target.atk * 0.2
            target.atk -= reduce_atk # Tan cong random dame - giam atk doi phuong
            print(f"[*] {self.name} ({self.chuc_vu()}) da dung ki nang danh ke dich: {target.name} ({target.chuc_vu()}) ({dame}st) va -{reduce_atk}atk ke dich", end = "")
            if self.marked_enemy == None:
                print(f" ke dich da bi {self.name} ({self.chuc_vu()}) danh dau")
                self.marked_enemy = target

        else:
            target.nhan_st(self.atk * 1.6)
            target.atk -= 3 # Tan cong va giam atk cua hero
            print(f"[*] {self.name} ({self.chuc_vu()}) da dung ki nang danh ke dich: {target.name} ({target.chuc_vu()}) ({self.atk*1.6}st) va -3atk ke dich")

    def tan_cong(self, target):
        super().tan_cong(target)
        if self.marked_enemy:
            self.marked_enemy.nhan_st(self.atk * 0.8)
            print(f"[*] {self.name} ({self.chuc_vu()}) tan cong vao ke bi danh dau: {target.name} ({target.chuc_vu()}) ({self.atk*0.8}st)")

    def chuc_vu(self):
        if self.type == 1:
            return 'Xac song thuong'
        elif self.type == 2:
            return 'Xac song mac giap'
        elif self.type == 3:
            return 'Xac song phu thuy'
        else:
            return 'Xac song khong lo'


# Passive Character - Multi Targets
class DarkDragon(Character):

    def __init__(self, name,  max_hp = 300, atk = 40):
        self.slot = 15
        super().__init__(name, max_hp, atk, 0)
        self.max_mn1_bs = 6 # +2atk + giam 50% mau + giet 1 hero + hero con lai bi -2atk va bi ratio*atk
        self.cur_mn1_bs = 6
        self.max_mn2_atk = 6 # Giam dame doi phuong + random dame + giam mau cua ban than
        self.cur_mn2_atk = 6
        self.max_mn3_de = 4 # tang dame vinh vien + giam mau 10% + danh doi phuong
        self.cur_mn3_de = 4

    def kiem_tra_day_mana(self):
        return self.cur_mn1_bs==self.max_mn1_bs or self.cur_mn2_atk==self.max_mn2_atk or self.cur_mn3_de==self.max_mn3_de

    def tang_mana(self):
        if self.cur_mn1_bs < self.max_mn1_bs:
            self.cur_mn1_bs += 1

        if self.cur_mn2_atk < self.max_mn2_atk:
            self.cur_mn2_atk += 1

        if self.cur_mn3_de < self.max_mn3_de:
            self.cur_mn3_de += 1

    # Tu dong random ki nang cho quai 
    def dung_ki_nang(self, targets):

        lst_skill = [1, 2, 3]

        if self.cur_mn1_bs < self.max_mn1_bs:
            lst_skill.remove(1)
        if self.cur_mn2_atk < self.max_mn2_atk:
            lst_skill.remove(2)
        if self.cur_mn3_de < self.max_mn3_de:
            lst_skill.remove(3)

        x = random.choice(lst_skill)
        ratio = self.get_hp() / self.get_max_hp()

        if x == 1:
            self.cur_mn1_bs = 0
            self.atk += 2
            reduce_hp = self.get_hp() * 0.5
            self.nhan_st(reduce_hp)
            marked_hero = random.choice(targets)
            marked_hero.nhan_st(marked_hero.get_hp())
            for hero in targets:
                if hero.atk > 2:
                    hero.atk -= 3
                hero.nhan_st(self.atk * ratio)
            print(f"[*] {self.name} ({self.chuc_vu()}) (+2atk)(-{reduce_hp}hp) tan cong vao toan bo ke dich ({self.atk*ratio}st) (-3atk) (tieu diet: {marked_hero.name} ({marked_hero.chuc_vu()}))")

        elif x == 2:
            self.cur_mn2_atk = 0
            self.nhan_st(30)
            random_dame = random.randint(40, 60)
            for hero in targets:
                hero.nhan_st(random_dame)
                hero.atk -= 2
            print(f"[*] {self.name} ({self.chuc_vu()}) (-30hp) tan cong vao toan bo ke dich ({random_dame}st) (-2atk)")
            
        else:
            self.cur_mn3_de = 0
            reduce_hp = self.get_hp() * 0.1
            self.nhan_st(reduce_hp)
            self.atk += 8
            for hero in targets:
                hero.nhan_st(self.atk)
            print(f"[*] {self.name} ({self.chuc_vu()}) (+8atk)(-{reduce_hp}hp) tan cong vao toan bo ke dich ({self.atk}st)")

    def chuc_vu(self):
        return 'Rong bong dem'
    
    def thong_tin(self):
        print(f"{self.name:<30} | {self.chuc_vu():<25} | {self._hp:>6}/{self._max_hp:>4} | ATK: {self.atk:<5} | Mn1: {self.cur_mn1_bs}/{self.max_mn1_bs} - Mn2: {self.cur_mn2_atk}/{self.max_mn2_atk} - Mn3: {self.cur_mn3_de}/{self.max_mn3_de}")


# Show danh sach nhan vat 
def show_lst_char(lst_char):
    count = 1
    for char in lst_char:
        print(f"{count:<2}. ", end = "")
        char.thong_tin()
        count += 1

# Nhap lst so nguyen gom number so trong [a;b]
def input_int_lst(a, b, number):
    while True:
        press = input("Nhap lua chon: ")
        lst_press = press.split()
        lst_index = []
        if len(lst_press) != number:
            print(f"Khong du so luong! Vui long nhap lai: ")
            continue
            
        for index in lst_press:
            try:
                index = int(index)
                if index < a or index > b:
                    raise Exception(f"Chi so duoc nhap phai nam trong doan [{a},{b}]")
                if index in lst_index:
                    raise Exception(f"Khong duoc nhap chi so trung nhau! Vui long nhap lai: ")
                lst_index.append(index)

            except ValueError:
                print(f"Cac chi so duoc nhap phai la so nguyen! Vui long nhap lai: ")
                break
            except Exception as e:
                print(e)
                break
                
        if len(lst_index) == number:
            break
    return lst_index
        

# Nhan vao 1 lst va bat nguoi dung chon hero cho wave nay
def choice_heros(lst_hero, number):
    print(f"--------------------------------------------------------------------------------------------------------------------")
    print(f"                                      Danh sach Hero con song: ")
    print(f"--------------------------------------------------------------------------------------------------------------------")
    show_lst_char(lst_hero)
    print(f"--------------------------------------------------------------------------------------------------------------------")
    print(f"Nhap cac tuong (so {1}-{len(lst_hero)})-(toi da {number} tuong) ban muon chon: ")
    lst_id_heros = input_int_lst(1, len(lst_hero), number)
    lst_choice_heros = []
    for id in lst_id_heros:
        lst_choice_heros.append(lst_hero[id-1])
    return lst_choice_heros


# Chon quai theo slot
def choice_monsters(lst_monsters, slot_number):
    lst = []
    chi_so = 1

    while slot_number > 0:  
        monster = random.choice(lst_monsters)
        if monster.slot <= slot_number:
            copied_monster = copy.deepcopy(monster)
            copied_monster.name += ' #' + str(chi_so)
            lst.append(copied_monster)
            chi_so += 1
            slot_number -= monster.slot

    return lst


# Hien thi menu chinh cua game
def main_menu():
    print(f"1. Game moi")
    print(f"2. Thoat game ")
    lst_choice = input_int_lst(1, 2, 1)
    return lst_choice[0]


# Hien thi ket qua sau moi turn danh
def show_result(lst_heros, lst_monsters):
    print(f"--------------------------------------------------------------------------------------------------------------------")
    print(f"KET QUA TRAN CHIEN : ")
    print(f"--------------------------------------------------------------------------------------------------------------------")
    print(f"Phe anh hung: ")
    for char in lst_heros:
        char.thong_tin()
    print(f"--------------------------------------------------------------------------------------------------------------------")
    print(f"Phe quai vat: ")
    for char in lst_monsters:
        char.thong_tin()

# Nhap '1' de den giai doan tiep theo
def continue_next_wave(wave):
    print(f"--------------------------------------------------------------------------------------------------------------------")
    print(f"Nhan '1' de vao (giai doan): {wave}")
    choice = input_int_lst(1,1,1)
    os.system('cls')

# Tinh chi so HP va ATK cua team
def caculate_team_stats(lst_char):
    sum_atk = 0
    sum_hp = 0

    for char in lst_char:
        sum_atk += char.atk
        sum_hp += char.get_max_hp()

    return sum_hp, sum_atk


def main():
    #data cho moi game
    lst_hero = [
        Warrior('HR1'),
        Tanker('HR2'),
        Healer('HR3'),
        Mage('HR4'),
        Priest('HR5'),
        Assassin('HR6'),
        PoisonMaster('HR7'),
        LifeStealer('HR8'),
        DarkKnight('HT9')
    ]

    lst_monster = [
        Orc('ORC nho', 1),
        Orc('ORC thuong', 2),
        Orc('ORC lon', 3),

        Golem('Golem', 1),
        Golem('Golem hac am', 2),

        GoblinAcher('Goblin lun', 1),
        GoblinAcher('Goblin thuy', 2),
        GoblinAcher('Goblin hoa', 3),

        ShadowAssassin('Sat thu ac ma'),

        Zombie('Zombie xau xi', 1),
        Zombie('Zombie binh thuong', 2),
        Zombie('Zombie phu thuy', 3),
        Zombie('Zombie dai ca', 4),

        DarkDragon('Rong hac am')
    ]


    while True:
        choice_main_menu = main_menu()

        if choice_main_menu == 1:
            lst_hero_alive = []
            for hero in lst_hero:
                deep_copy_hero = copy.deepcopy(hero)
                lst_hero_alive.append(deep_copy_hero)
            wave = 1
            result = 2
            slot_monsters = 3
            slot_heros = 4
            os.system("cls")
            while True:
                if result == 0:
                    break
                if result == 1:
                    result = 2
                
                print(f"Wave: {wave}                                GIAI DOAN CHON TUONG (WAVE MOI)")
                print(f"--------------------------------------------------------------------------------------------------------------------")
                slot_monsters += 3
                if wave % 5 == 0: slot_heros += 1 
                print(f"DANH SACH QUAI LUOT NAY: ")
                # Khoi tao danh sach quai vat
                lst_original_chosen_monsters = choice_monsters(lst_monster,slot_monsters)
                lst_chosen_monsters = lst_original_chosen_monsters.copy()
                show_lst_char(lst_chosen_monsters) 

                sum_hp_monsters, sum_atk_monsters = caculate_team_stats(lst_original_chosen_monsters)
                print(f"-> Tong mau: {sum_hp_monsters}   -   Tong luc chien: {sum_atk_monsters}")

                print(f"--------------------------------------------------------------------------------------------------------------------")
                print(f"HAY CHON TUONG CHO VAN NAY (THU TU CHON TUONG SE LA THU TU TAN CONG): ")
                lst_original_chosen_heros = choice_heros(lst_hero_alive,slot_heros )
                lst_chosen_heros = lst_original_chosen_heros.copy()
                print(f"--------------------------------------------------------------------------------------------------------------------")
                print(f"Danh sach cac tuong da chon: ")
                print(f"--------------------------------------------------------------------------------------------------------------------")
                show_lst_char(lst_chosen_heros)

                sum_hp_heros, sum_atk_heros = caculate_team_stats(lst_original_chosen_heros) 
                print(f"-> Tong mau: {sum_hp_heros}   -   Tong luc chien: {sum_atk_heros}")

                # Chon tuong dung ki nang -> bat dau tran dau -> Chon tuong dung ki nang 
                print(f"--------------------------------------------------------------------------------------------------------------------")
                continue_next_wave('Chuan bi')
                turn = 1
                while True:
                    if result == 0 or result == 1:
                        break
                    print(f"--------------------------------------------------------------------------------------------------------------------")
                    print(f"Wave: {wave} - Turn: {turn}                       GIAI DOAN CHUAN BI")
                    print(f"--------------------------------------------------------------------------------------------------------------------")
                    print(f"Danh sach quai trong turn nay: ")
                    show_lst_char(lst_chosen_monsters)
                    print(f"--------------------------------------------------------------------------------------------------------------------")

                    lst_available_skills = []
                    chosen_hero = None
                    target_monster = None

                    for char in lst_chosen_heros:
                        if char.kiem_tra_day_mana() is True:
                            lst_available_skills.append(char)

                    # Kiem tra neu co tuong nao con skill thi cho chon
                    if lst_available_skills:
                        print(f"Chon tuong de su dung ki nang (chon 0 de khong dung) (ki nang chi kich hoat khi den luot danh cua tuong): ")
                        print(f"--------------------------------------------------------------------------------------------------------------------")
                        print(f"Danh sach cac tuong co the su dung ki nang:")
                        show_lst_char(lst_available_skills)
                        print(f"--------------------------------------------------------------------------------------------------------------------")
                        choice_index_skill = input_int_lst(0, len(lst_available_skills), 1)

                        if choice_index_skill[0] == 0:
                            print(f"Ban da chon khong dung ki nang cua cac tuong")
                        else:
                            chosen_hero = lst_available_skills[choice_index_skill[0]-1]
                            print(f"Ban da chon tuong: {chosen_hero.name} ({chosen_hero.chuc_vu()})")

                            # Chon muc tieu cho cac tuong don muc tieu
                            if isinstance(chosen_hero, (Healer, Priest)):
                                print(f"--------------------------------------------------------------------------------------------------------------------")
                                print(f"Chon muc tieu de su dung ki nang: ")
                                show_lst_char(lst_chosen_heros)
                                print(f"--------------------------------------------------------------------------------------------------------------------")
                                print(f"Chon tuong muc tieu muon buff (1-{len(lst_chosen_heros)}): ")
                                index_hero = input_int_lst(1, len(lst_chosen_heros), 1)
                                target_hero = lst_chosen_heros[index_hero[0]-1]

                            elif not isinstance(chosen_hero, (Tanker, Mage)):
                                print(f"--------------------------------------------------------------------------------------------------------------------")
                                print(f"Chon muc tieu de su dung ki nang: ")
                                print(f"--------------------------------------------------------------------------------------------------------------------")
                                print(f"Chon quai lam muc tieu (1-{len(lst_chosen_monsters)}): ")
                                index_monster = input_int_lst(1, len(lst_chosen_monsters), 1)
                                target_monster = lst_chosen_monsters[index_monster[0]-1]

                            # Muc tieu cua tuong da muc tieu
                            else:
                                target_monster = lst_chosen_monsters 

                    else:
                        print(f"Ki nang cua cac tuong dang trong thoi gian hoi")

                    continue_next_wave('Chien dau')

                    print(f"--------------------------------------------------------------------------------------------------------------------")
                    print(f"Wave: {wave} - Turn: {turn}                    GIAI DOAN CHIEN DAU")
                    print(f"--------------------------------------------------------------------------------------------------------------------")
                    # Cho hero danh lan luot roi den monster danh
                    # Danh: Chon target random -> Danh target -> tang mana -> Quai chon target random (Chon ngay trong luot danh) -> Danh target -> Tang mana
                    # Neu duyet vao char duoc chon thi: Dung ki nang -> Tiep tuc den voi char khac
                    
                    # Hero Tan cong
                    for char in lst_chosen_heros:
                        char.tang_mana()
                        # Char khac hero duoc chon dung ki nang
                        if char != chosen_hero:
                            if not lst_chosen_monsters:
                                print(f"Het muc tieu")
                                continue
                            target = random.choice(lst_chosen_monsters)
                            char.tan_cong(target)
                            if not target.con_song():
                                lst_chosen_monsters.remove(target)
                        # Hero dung ki nang -> target_monster
                        else:
                            if isinstance(char, (Healer, Priest)):
                                char.dung_ki_nang(target_hero)
                            else:
                                char.dung_ki_nang(target_monster)
                                if not isinstance(target_monster, list) and target_monster.con_song() is False and target_monster in lst_chosen_monsters:
                                    lst_chosen_monsters.remove(target_monster)
                                if isinstance(target_monster, list):
                                    for monster in target_monster[:]:
                                        if not monster.con_song():
                                            lst_chosen_monsters.remove(monster)

                    for char in lst_chosen_heros:
                        if isinstance(char, DarkKnight):
                            char.check_marked_enemy()
                            break

                    print(f"              ---------------------------------------------------------------------------")

                    # Chon quai dung skill
                    lst_available_skills = []
                    for monster in lst_chosen_monsters:
                        if monster.kiem_tra_day_mana():
                            lst_available_skills.append(monster)

                    random_chosen_monster = None
                    if lst_available_skills:
                        random_chosen_monster = random.choice(lst_available_skills)

                    # Quai tan cong
                    for char in lst_chosen_monsters:
                        char.tang_mana()
                        if not lst_chosen_heros:
                            break
                        # Chon quai de dung ki nang
                        if char == random_chosen_monster:
                            # Quai don muc tieu
                            if not isinstance(char, DarkDragon):
                                if isinstance(chosen_hero, Tanker):
                                    char.dung_ki_nang(chosen_hero)
                                    if not chosen_hero.con_song():
                                        lst_chosen_heros.remove(chosen_hero)
                                else:
                                    target = random.choice(lst_chosen_heros)
                                    char.dung_ki_nang(target)
                                    if not target.con_song():
                                        lst_chosen_heros.remove(target)
                            # Quai da muc tieu
                            else:
                                char.dung_ki_nang(lst_chosen_heros)
                                for hero in lst_chosen_heros[:]:
                                    if not hero.con_song():
                                        lst_chosen_heros.remove(hero)

                        # Quai thuong -> chosen_hero or target random
                        else:
                            if isinstance(chosen_hero, Tanker):
                                char.tan_cong(chosen_hero)
                                if not chosen_hero.con_song():
                                    lst_chosen_heros.remove(chosen_hero)
                            else:
                                target = random.choice(lst_chosen_heros)
                                char.tan_cong(target)
                                if not target.con_song():
                                    lst_chosen_heros.remove(target)


                    #Hien ket qua
                    show_result(lst_original_chosen_heros, lst_original_chosen_monsters)         

                    if not lst_chosen_heros:
                        result = 0
                    if not lst_chosen_monsters:
                        for hero in lst_original_chosen_heros:
                            hero.hoi_mau(hero.get_max_hp() * 0.17)
                        result = 1

                    if result == 0 or result == 1:
                        print(f"--------------------------------------------------------------------------------------------------------------------")
                        print(f"KET QUA CHUNG CUOC: ", f"WIN" if result else "LOSE")
                        if result:
                            wave += 1
                            continue_next_wave('Chon tuong cho wave moi')
                        else:
                            continue_next_wave('Menu')
                    else:
                        turn += 1
                        continue_next_wave('Chuan bi cho turn danh tiep theo')

                
        else:
            os.system("cls")
            print(f"BAN DA THOAT TRO CHOI")
            break

main()
