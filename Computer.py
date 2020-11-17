'''class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram


    def config(self):
        print("Config is ", self.cpu, self.ram)

com1 = Computer('i5', 16)
com2 = Computer('Ryzen 3', 8)

com1.config()
com2.config()'''
class Computer:

    def __init__(self):
        self.name = "Thabang"
        self.age = 23

    def update(self):
        self.name = 24

    def compare(self, c2):
        if self.age == c2.age:
            return True
        else:
            return False



c1 = Computer()
c1.age = 24
c2 = Computer()

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")


c1.update()

print(c1.name)





