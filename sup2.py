class Human:
    def __init__(self, name, age):
        self.n = name
        self.a = age
    def talk(self, talk):
        print("я мухамеда самира лучши таксиста в мира")
    def PrintInfo(self):
        print(f"именниk {self.n}, годики {self.a}")

class Taxi(Human):
    def __init__(self, name, age, lunch):
        super().__init__(name, age)
        self.lunch = lunch
    def work(self):
        print("рабу надо работать")
    def talk(self):
        print("салам я мухамеда таксиста от бога")
    def PrintInfo(self):
        print(f"именник {self.n}, гадов {self.a}, жратва {self.lunch}")
Taxi = Taxi("Мухамеда", 42, "сэндвич")
Taxi.talk()
Taxi.PrintInfo()
Taxi.work()

class car:
    def drive(self):
        print("The car is driving")
class plane:
    def fly(self):
        print("The plane is flying")
class FlyingCar(car, plane):
    def drive(self):
        pass

    def show_abilities(self):
        super().drive()
        super().fly()
    
q = FlyingCar()
q.show_abilities()