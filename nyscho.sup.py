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
