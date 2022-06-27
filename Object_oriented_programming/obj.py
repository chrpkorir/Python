
"""def hi(obj):
    print("Hello, I am" + obj.name)


class Robot:
    say_hi = hi  # bind function hi to class attribute say_hi


x = Robot()
x.name = "Marvin"
Robot.say_hi(x)
"""
"""
Correct way
"""
class Robot:

    def __init__(self, name):
        self.name = name

    def hi(self):
        print("Hello, I am", self.name)

x = Robot('Marvin')
x.hi()
