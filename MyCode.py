
class Father:

    def func1(self):
        print("Father Func 1")

    def func2(self):
        print("Father Func 2")

class Son(Father):

    def func3(self):
        print("son Func 3")

    def func4(self):
        print("son Func 4")

class SonOfSon(Son):

       def printSon(self):
           print("son of son Func")

Mohamed = SonOfSon()
Mohamed.func1()
