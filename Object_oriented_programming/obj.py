def hi(obj):
    print("Hello, I am" + obj.name + "!")


class Robot:
    pass


x = Robot()
x.name = "Marvin"
hi(x)
