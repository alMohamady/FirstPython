

class Car:

    seats = 4

    def __init__(self):
        self.name = "golf"
        self.speed = 180


polo = Car()
mini = Car()

Car.seats = 2

print(polo.seats)
print(mini.seats)


