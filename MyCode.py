
class A:

    def __init__(self):
        print("this is init A")

    def func1(self):
        print ("this is func a1")

    def func2(self):
        print ("this is func a2")

class B:

    def __init__(self):
        print("this is init B")

    def func3(self):
        print("this is func b3")

    def func4(self):
        print("this is func b4")

class C(A,B):

    def __init__(self):
        super().__init__()
        print("this is init C")

    def func5(self):
        print("this is func c5")

obj = C()
