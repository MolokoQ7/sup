class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def is_square(self):
        return self.width == self.height

r1 = Rectangle(5, 10)
print("Площа:", r1.area())
print("Its kvadrat?", r1.is_square())

r2 = Rectangle(7, 7)
print("Площа:", r2.area())
print("Its kvadrat?", r2.is_square())


class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

class Book:
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author

    def get_description(self):
        return f"Книга '{self.title}' написана автором {self.author.name} з {self.author.nationality}"

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def info(self):
        return f"{self.name}, зарплата: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def info(self):
        return f"{self.name}, зарплата: {self.salary}, бонус: {self.bonus}"


a = Author("Леся Українка", "Україна")
b = Book("Лісова пісня", 1911, a)
print(b.get_description())

e = Employee("Марія", 18000)
print(e.info())


m = Manager("Олександр", 25000, 4000)
print(m.info())




from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def info(self):
        pass

class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} car is driving on the road.")

    def info(self):
        print(f"This is a car. Brand: {self.brand}")

class Bike(Vehicle):
    def drive(self):
        print(f"{self.brand} bike is riding on the track.")

    def info(self):
        print(f"This is a bike. Brand: {self.brand}")

car = Car("Toyota")
bike = Bike("Yamaha")

car.drive()
car.info()

bike.drive()
bike.info()


from abc import ABC, abstractmethod

class Instrument(ABC):
    @abstractmethod
    def play(self):
        pass

class Guitar(Instrument):
    def play(self):
        print("Гітара грає акорди")

class Piano(Instrument):
    def play(self):
        print("Піаніно грає мелодію")

instruments = [Guitar(), Piano()]

for instrument in instruments:
    instrument.play()



from abc import ABC, abstractmethod

class Pet(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self):
        pass

    def info(self):
        return f"Ім'я: {self.name}, Вік: {self.age}"

class Dog(Pet):
    def make_sound(self):
        print("Гав-гав!")

    def info(self):
        return super().info() + " | Тип: Пес"

class Cat(Pet):
    def make_sound(self):
        print("Няв-няв!")

    def info(self):
        return super().info() + " | Тип: Кіт"

class Product(ABC):
    def __init__(self, name, base_price):
        if base_price <= 0:
            raise ValueError("Ціна повинна бути > 0")
        self.name = name
        self.base_price = base_price

    @abstractmethod
    def get_final_price(self):
        pass

class BookProduct(Product):
    def get_final_price(self):
        return self.base_price * 0.9

class ElectronicProduct(Product):
    def get_final_price(self):
        if self.base_price < 500:
            return self.base_price
        return self.base_price * 0.95

pets = [Dog("Шарик", 3), Cat("Мурчик", 2)]
for pet in pets:
    print(pet.info())
    pet.make_sound()

try:
    products = [
        BookProduct("Книга", 300),
        ElectronicProduct("Телевізор", 600),
        ElectronicProduct("Телефон", 400)
    ]
    for product in products:
        print(f"{product.name}: {product.get_final_price()} грн")
except ValueError as e:
    print(e)
