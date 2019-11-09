
class Duck:

    def quack(self):
        print("duck is quacking")

class Hen:

    def quack(self):
        print("hen is quacking")

class Farm:

    def getSound(self, animal):
        animal.quack()

myFarm = Farm()
d = Duck()
h = Hen()
myFarm.getSound(h)