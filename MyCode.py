

class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        stu = Student(m1, m2)
        return stu

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return " {} and {} ".format(self.m1, self.m2)

ahmed = Student(100, 90)
mohmed = Student(180, 50)

stu = ahmed + mohmed
print(stu.m1, stu.m2)

if ahmed > mohmed:
    print("ahemd  wins")
else:
    print("mohamed wins")

a = 10
print(a.__str__())
print(ahmed.__str__())