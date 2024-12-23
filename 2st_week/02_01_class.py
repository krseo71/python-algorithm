
class Person:
    def __init__(self, name_param):
        self.name = name_param
        print(self.name)

    def talk(self):
        print("I am talking")


person_1 = Person("유재석")
person_1.talk()

person_2 = Person("박명수")

