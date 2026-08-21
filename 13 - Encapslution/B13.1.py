class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, amount):
        if amount < 0: print(f"So du khong the am")
        else: self.__balance = amount
    

p = BankAccount("quan", 1921)
print(f"{p.get_balance()}")
p.set_balance(2000)
print(f"{p.get_balance()}")
