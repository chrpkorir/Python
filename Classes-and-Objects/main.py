class Student:
    # [assignment] Skeleton class. Add your code here

    def __init__(self, name, age, tracks, score):
        pass

    def change_name(self, name):
        self.name = name

    def change_age(self, age):
        self.age = age

    def add_track(self, tracks):
        self.track = tracks

    def get_score(self,score):
        self.score = score

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")

Bob.get_score(20.90)
