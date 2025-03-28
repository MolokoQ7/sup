class human:
    def __init__(self, name, age):
        self.n = name
        self.a = 0

class Bus:
    def __init__(self):
        self.passengers = []
    def  Add_passengers(self, human):
        self.passengers.append(human)
    def Printpassenger(self):
        for human in self.passengers:
            print(human.name, human.age)
h1 = human("sanya",18)
h2 = human("mark",20)
b = Bus()
b.Add_passengers(h1)
b.Add_passengers(h2)
