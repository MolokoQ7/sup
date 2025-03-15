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

class Student:
    def __init__(s, n, m=0): s.n, s.g, s.gr = n, [], m
    def A(s, g): s.g.append(g)
    def G(s): return sum(s.g) / len(s.g) if s.g else 0
    def add_gr(s, m): s.gr += m
    def take_gr(s, m): s.gr -= m

s = Student("Росомаха")
s.A(10)
s.A(8)
s.A(9)
s.add_gr(100)
s.take_gr(50)
print(s.n, s.G(), s.gr)