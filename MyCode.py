

class Student:

    School = "MSC"

    def __init__(self, math, science, lang):
        self.math = math
        self.science = science
        self.lang = lang

    def avg(self):
        return (self.math + self.science + self.lang) / 3

    def get_math(self):
        return self.math

    def set_math(self, math):
        self.math = math

    @classmethod
    def get_info(cls):
        return cls.School


print(Student.get_info())


