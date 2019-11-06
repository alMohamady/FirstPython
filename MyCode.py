

class Car:

    def __init__(self, name, speed):
        print("Hello there ", name, speed)
        self.name = name
        self.speed = speed

    def drive(self):
        print("Driving the car", self.name, self.speed)


a = 8
polo = Car("polo", 180)
mini = Car("mini", 200)

polo.drive()
mini.drive()