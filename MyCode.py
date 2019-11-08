

class Car:

    def __init__(self, model, kilos, cc, liters):
        self.model = model
        self.kilos = kilos
        self.engine = self.Engine(cc, liters)

    def show(self):
        print(self.model, self.kilos)
        print(self.engine.show())


    class Engine:

        def __init__(self, cc, liters):
            self.cc = cc
            self.liters = liters

        def show(self):
            print(self.cc, self.liters)


mini = Car("MINI", 120, 1200, 40)
eng = Car.Engine(1600, 80)

print(eng.show())

