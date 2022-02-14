from datetime import date
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def fromBirthyear(cls,name,year):
        return cls(name,date.today().year-year)
    @staticmethod
    def isAdult(age):
        return age>18
person1= Person('john',21)
person2= Person.fromBirthyear('tom',1995)
print(person1.age,person2.age,Person.isAdult(22))
# print(Person.isAdult(22))

