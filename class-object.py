class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def setschool(self, school):
        self.school = school

    def getSchool(self):
        return self.school

    def random(self):
        print("My name is", self.name)
        print("My age is", self.age)


demo_person = Person('Nathan', 27)
demo_person.setschool("Oxford")

print(demo_person.age)
demo_person.random()
print(demo_person.getSchool())
