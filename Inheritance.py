
class A:                                # Super/Parent Class

    def __init__(self):
        print("in A Init")

    def feature1(self):
        print("Feature 1-A working")

    def feature2(self):
            print("Feature 2 working")

class B:

    def __init__(self):
#       super().__init__()  The moment you say super(). you are calling a feature in the super class
        print("in B Init")

    def feature1(self):
        print("Feature 1-B working")

    def feature4(self):
            print("Feature 4 working")

class C(A, B):

    def __init__(self):
        super().__init__() # Method Resolution Order (MRO)
        print("in C Init")

    def feat(self):
        super().feature2()


a1 = C()
a1.feature1()
a1.feat()






'''
from Chef import Chef
from ChineseChef import ChineseChef

class C(A, B):                             # Sub/Child Class
    def feature5(self):
        print("Feature 5 working")

a1 = A()
a1.feature2()

b1 = B()
b1.feature3()

c1 = C()
c1.feature4()

myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_salad()
myChineseChef.make_special_dish()

'''