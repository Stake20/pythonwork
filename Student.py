
class Student:

    def __init__(self, name, major, gpa):
        self.name = name    # self.name the actual objects name will be equal to the name that's being passed in
        self.major = major  # the major of the student object will be equal to the major that was passed in
        self.gpa = gpa

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

    def greetings(self):
        return f'My name is {self.name} and I have a {self.gpa} GPA'



class Senior (Student):

    def __init__(self, name, major, gpa):
        self.name = name    # self.name the actual objects name will be equal to the name that's being passed in
        self.major = major  # the major of the student object will be equal to the major that was passed in
        self.gpa = gpa
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greetings(self):
        return f'My name is {self.name} and I have a {self.gpa} GPA and my balance is {self.balance}'