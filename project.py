class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def info(self):
        return f"{self.name}: ${self.price}"

class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = []
    def add(self, product):
        self.cart.append(product)
        print(f"+ {product.name}")
    def show(self):
        if not self.cart:
            print("Кошик них##.")
            return
        total = sum(p.price for p in self.cart)
        print(f"Кошик {self.name}:")
        for p in self.cart:
            print(p.info())
        print(f"Всього: ${total}")

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def make_sound(self):
        print(f"{self.name} видає звук: {self.sound}")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Гав гав")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Мяу мяу")

if __name__ == "__main__":
    c = Customer("Геніус")
    c.add(Product("Яблучко", 1.5))
    c.add(Product("Хліб", 2.0))
    c.show()
    Dog("Рекс").make_sound()
    Cat("Мурчик").make_sound()
