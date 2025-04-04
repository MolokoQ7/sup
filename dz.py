class Calculator:
    def __init__(self, a, b):
        if type(a) not in (int, float) or type(b) not in (int, float):
            raise TypeError("Аргументи мають бути числами.")
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            raise ZeroDivisionError("Ділення на нуль неможливе.")
        return self.a / self.b


calc = Calculator(10, 2)
print(calc.add())       # 12
print(calc.subtract())  # 8
print(calc.multiply())  # 20
print(calc.divide())    # 5.0
