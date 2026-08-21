from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, owner, balance, account_number):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance
    
    @abstractmethod
    def tinh_lai_suat(self):
        pass

    @abstractmethod
    def thong_tin(self):
        pass

    def nap_tien(self, amount):
        if amount < 0:
            raise Exception(f"So tien nap vao khong the am")
        else:
            self.__balance += amount
    
    def rut_tien(self, amount):
        if amount < 0: 
            raise Exception(f"So tien rut ra khong the be hon 0")
        else:
            if amount > self.__balance:
                raise Exception(f"So tien rut ra khong the lon hon so du")
            else:
                self.__balance -= amount
    
    def get_balance(self):
        return self.__balance

    def change_balance(self, amount):
        self.__balance += amount

    def ap_dung_lai_suat(self):
        self.__balance *= (1 + self.tinh_lai_suat())


class SavingsAccount(Account):
    def __init__(self, owner, balance, account_number):
        super().__init__(owner, balance, account_number)
        self.__withdraw_count = 0   
    

    def tinh_lai_suat(self):
        return 0.05
    
    
    def rut_tien(self, amount):
        if amount < 0:
            raise Exception("So tien rut khong the am")
        
        if self.__withdraw_count >= 2:
            raise Exception("Chỉ được rút tối đa 2 lần mỗi tháng")

        super().rut_tien(amount)
        self.__withdraw_count += 1


    def thong_tin(self):
        print(f"Loai tai khoan: Tai khoan tiet kiem")
        print(f"Chu tai khoan: {self.owner}")
        print(f"So du: {self.get_balance()} - Lai suat: {self.tinh_lai_suat()}")
        print(f"So tai khoan: {self.account_number}")


class CheckingAccount(Account):
    def __init__(self, owner, balance, account_number):
        super().__init__(owner, balance, account_number)
    
    def tinh_lai_suat(self):
        return 0.01

    def rut_tien(self, amount):
        if amount < 0: 
            raise Exception("So tien rut khong the am")
        
        if self.get_balance() - amount < -500000:
            raise Exception("So du toi thieu phai lon hon hoac bang -500000")
        
        self.change_balance(-amount)
        
    def thong_tin(self):
        print(f"Loai tai khoan: Tai khoan giao dich")
        print(f"Chu tai khoan: {self.owner}")
        print(f"So du: {self.get_balance()} - Lai suat: {self.tinh_lai_suat()}")
        print(f"So tai khoan: {self.account_number}")


class Bank:
    def __init__(self, name):
        self.name = name
        self.__accounts = []
    
    def them_tai_khoan(self, account):
        if self.tim_theo_so_tai_khoan(account.account_number):
            raise Exception("So tai khoan da ton tai")
        self.__accounts.append(account)

    def mo_tai_khoan(self, account):
        if account in self.__accounts:
            account.thong_tin()
        
    def tong_tien_toan_bank(self):
        total = 0
        for item in self.__accounts:
            total += item.get_balance()
        return total

    def ap_dung_lai_suat_toan_bank(self):
        for item in self.__accounts:
            item.ap_dung_lai_suat()

    def tim_theo_so_tai_khoan(self, number):
        for item in self.__accounts:
            if item.account_number == number:
                return item
        return None
    
    def danh_sach_savings_account(self):
        lst_SA = []
        for item in self.__accounts:
            if isinstance(item, SavingsAccount):
                lst_SA.append(item)
        return lst_SA

    def danh_sach_checking_account(self):
        lst_CA = []
        for item in self.__accounts:
            if isinstance(item, CheckingAccount):
                lst_CA.append(item)
        return lst_CA
    
    def thong_tin(self):
        lst_SA = self.danh_sach_savings_account()
        lst_CA = self.danh_sach_checking_account()
        print(f"Ngan hang: {self.name}")
        print(f"---------------------------------------")
        print(f"SavingsAccount: ")
        print(f"---------------------------------------")
        for item in lst_SA:
            item.thong_tin()
            print(f"---------------------------------------")
        print(f"CheckingAccount: ")
        print(f"---------------------------------------")
        for item in lst_CA:
            item.thong_tin()
            print(f"---------------------------------------")

    def sao_luu(self, filename):
        with open(filename, 'w') as f:
            f.write(f"Ten ngan hang: {self.name}\n")
            
            lst_SA = self.danh_sach_savings_account()
            lst_CA = self.danh_sach_checking_account()
            
            f.write(f"---------------------------------------\n")
            f.write(f"Danh sach: Tai khoan tiet kiem\n")
            f.write(f"---------------------------------------\n")
            for item in lst_SA:
                f.write(f"Chu tai khoan: {item.owner:<20} - So tai khoan: {item.account_number:<15} - So du: {item.get_balance():<15}\n")

            f.write(f"---------------------------------------\n")
            f.write(f"Danh sach: Tai khoan giao dich\n")
            f.write(f"---------------------------------------\n") 
            for item in lst_CA:
                f.write(f"Chu tai khoan: {item.owner:<20} - So tai khoan: {item.account_number:<15} - So du: {item.get_balance():<15}\n")

    def phuc_hoi(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                print(line.strip())


def main():

    # Tao tai khoan
    lst_accounts = [
        SavingsAccount('Quan', 2000000, '34248798798'), #0
        SavingsAccount('Nhi', 4000000, '34248798797'),
        SavingsAccount('Hoang', 5000000, '34248798796'),
        SavingsAccount('Tuan', 555000, '34248798790'),

        CheckingAccount('Hung', 3000000, '44248798798'),
        CheckingAccount('An', 15000000, '54248798798'),
        CheckingAccount('Bac', 90000000, '64248798798'),
        CheckingAccount('Xuan', 19000000, '74248798798'),
        CheckingAccount('Vuong', 21000000, '84248798798') #8
    ]

    # Thuc hien giao dich rut tien
    try:
        lst_accounts[3].rut_tien(5000000)
        print(f"Rut tien thanh cong")
    except Exception as e:
        print(e)

    # Thuc hien giao dich nap tien
    try:
        lst_accounts[7].nap_tien(809890)
        print(f"Nap tien thanh cong")
    except Exception as p:
        print(p)

    # Them tai khoan vao bank
    bank = Bank('Agribank')
    for item in lst_accounts:
        try:
            bank.them_tai_khoan(item)
        except Exception as p:
            print(p)
    
    # Ap dung lai suat toan bank, in tong tien truoc/sau khi ap dung lai suat
    print(f"\n\n\nSO TIEN TOAN NGAN HANG TRUOC KHI AP DUNG LAI SUAT\n\n\n")
    bank.thong_tin()
    print(f"TONG SO TIEN TOAN NGAN HANG LA: {bank.tong_tien_toan_bank()}")
    
    bank.ap_dung_lai_suat_toan_bank()

    print(f"\n\n\nSO TIEN TOAN NGAN HANG SAU KHI AP DUNG LAI SUAT\n\n\n")
    bank.thong_tin()
    print(f"TONG SO TIEN TOAN NGAN HANG LA: {bank.tong_tien_toan_bank()}")

    # Sao luu ra file 
    bank.sao_luu('EX15_5.txt')
main()