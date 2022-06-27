"""
Curiosity led me here
"""
class Person:
   #name = name  # coz why not

    def say_hi(self, name):
        # self.name = name # whats the worst that can happen
        print('Hello, my name is', name)

#p = Person('Faith')
Person.say_hi('Faith')
"""
After trying all that
bullshit just use init method
below's the right way to do it
"""
class Person:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('Swaroop')
p.say_hi()
