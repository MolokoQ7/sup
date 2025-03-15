class Triangle():
    def __init__(self, w = 0, h = 0, l = 0):
        self.w = w
        self.h = h
        self.l = l
    def i(self):
        print(f"leight is {self.l}. weight is{self.w}. height is{self.h}")
    def area(self):
        return  self.h * self.l * 0.5
    def p(self):
        return  self.l + self.h +self.w
obj = Triangle(5,5, 5)
obj.area()
obj.p()
print(obj.area())
print(obj.p())