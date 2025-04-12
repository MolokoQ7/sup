
#типа че как мабой 1 завдання
class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def info(self):
        return self.brand, self.model, self.year, self.mileage

    def drive(self, distance):
        self.mileage += distance

    def is_old(self):
        return self.year < 2010

class Garage:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
    def drive_all(self, distance):
        for car in self.cars:
            car.drive(distance)
    def show_all(self):
        for car in self.cars:
            print(car.info())
    def show_old_cars(self):
        for car in self.cars:
            if car.is_old():
                print(car.info())

car1 = Car("BMW", "X5", 2005, 200000)
car2 = Car("Tesla", "Model 3", 2020, 30000)
garage = Garage()
garage.add_car(car1)
garage.add_car(car2)
garage.drive_all(100)
garage.show_all()
garage.show_old_cars()


# ну тіпа йоу мабой 2 завдання


from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title, year):
        self.title = title
        self.year = year

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def is_old(self):
        pass


class Book(LibraryItem):
    def __init__(self, title, year, author, pages):
        super().__init__(title, year)
        self.author = author
        self.pages = pages

    def info(self):
        return self.title, self.author, self.year, self.pages

    def is_old(self):
        return self.year < 2000


class Magazine(LibraryItem):
    def __init__(self, title, year, issue_number, month):
        super().__init__(title, year)
        self.issue_number = issue_number
        self.month = month

    def info(self):
        return self.title, self.issue_number, self.month, self.year

    def is_old(self):
        return self.year < 2015


class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if not isinstance(item, LibraryItem):
            raise TypeError("тільки LibraryItem")
        self.items.append(item)

    def show_all(self):
        for item in self.items:
            print(item.info())

    def show_old(self):
        for item in self.items:
            if item.is_old():
                print(item.info())

    def find_by_title(self, word):
        for item in self.items:
            if word.lower() in item.title.lower():
                print(item.info())


#ну тіпа йоу 3 завдання


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return self.name, self.price

class FoodItem(Item):
    def __init__(self, name, price, expiration_date):
        super().__init__(name, price)
        self.expiration_date = expiration_date

    def get_info(self):
        return self.name, self.price, self.expiration_date

class TechItem(Item):
    def __init__(self, name, price, warranty_years):
        super().__init__(name, price)
        self.warranty_years = warranty_years

    def get_info(self):
        return self.name, self.price, self.warranty_years

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_cart(self):
        for item in self.items:
            print(item.get_info())

    def total_price(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

class Shopper:
    def __init__(self, name):
        self.name = name
        self.cart = ShoppingCart()

    def add_to_cart(self, item):
        self.cart.add_item(item)

    def checkout(self):
        self.cart.show_cart()
        print(f"Загальна сума: {self.cart.total_price()} грн")
