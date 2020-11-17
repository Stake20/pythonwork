
class Student:

    school = 'Bernadino Heights'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3


    def avg(self):                              # Instance method
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):                           # Accessor/Getters
        return self.m1

    def set_m1(self, value):                    # Mutators/Setters
        self.m1 = value

    @classmethod
    def getSchool(cls):                         # Class method
        return cls.school

    @staticmethod
    def info():                                 # Static method
        print("This is student class. . In abc module")


s1 = Student(34,67,32)
s2 = Student(89,32,12)
print(s1.avg())
print(Student.getSchool())