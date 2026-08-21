class Product:
    discount_rate = 0.1

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount_price(self):
        return self.price * (1 - Product.discount_rate)
    
    def show(self):
        print(f"Ten: {self.name} - Gia goc: {self.price} - Gia sau giam: {self.discount_price()}")


p1 = Product("May hut bui", 199000)
p1.show()