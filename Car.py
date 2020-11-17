class Car:
    wheels = 5              # Class/Static variables

    def __init__(self):
        self.mileage = 10   # Instance Variabes
        self.company = "BMW"

c1 = Car()
c2 = Car()

print(c1.company, c1.mileage, c1.wheels)
c2.mileage = 25
Car.wheels = 4
print(c2.company, c2.mileage, c2.wheels)