
class Father:

      def info(self):
          print("Father Info")

class Student(Father):

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def info(self):
        super().info()
        print("Son Info")

    def sum(self, a=None, b=None, c=None):

        if a != None and b != None and c != None:
            d = a + b + c
        elif  a != None and b != None:
            d = a + b
        elif  a != None:
            d = a

        return d

st= Student(1, 2)

print(st.info())

print(st.sum(1+2+3))
print(st.sum(1+2))
print(st.sum(1))