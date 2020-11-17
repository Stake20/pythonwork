class Student:

    def __init__(self,name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = 'Lenovo'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)



s1 = Student('Thabang', 2)
s2 = Student('Timothy', 3)
lap1 = Student.Laptop()

s1.show()
print(s1.lap.brand)