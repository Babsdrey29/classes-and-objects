class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(mine, name, age, track, score):
        mine.name = str(name)
        mine.age = int(age)
        mine.tracks = list(track)
        mine.score = float(score)

    def myfunc(mine):
      print("Hello my name is " + mine.name)
    def change_name(mine, n_name):
        mine.name = n_name
    def change_age(mine, n_age):
        mine.age = n_age
    def add_track(mine, n_track):
        mine.track = n_track
    def get_score(mine, n_score):
        mine.score = n_score


n_name = "peter"
n_age = 34
n_track = ["UI/UX"]
n_score = 9.0  
print("the student new name is:", n_name)
print(f"the student new age is:", n_age)
print(f"the student new track is:", n_track)
print(f"the student new score is:", n_score)

Bob = Student(name="Bob", age=26, track=["FE","BE"],score=20.90)

Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(9.0)



