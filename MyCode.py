

class Car:

    def __init__(self):
        self.name = "golf"
        self.speed = 180

    def update(self):
        self.name = "passat"

    def compare(self, other):
        if self.name == other.name:
            return True
        else:
            return False

polo = Car()
mini = Car()

print(polo.name)
print(mini.name)

if polo.compare(mini):
    print("they are same")

