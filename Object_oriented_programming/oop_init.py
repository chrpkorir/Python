class Person:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hello, my name is", self.name)


p = Person('Swaroop') # Create an instance p of a class Person
p.say_hi()
# The previous 2 lines can also be written as
# Person('Swaroop).say_hi()
