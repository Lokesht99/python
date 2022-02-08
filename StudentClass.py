class Student:
    marks=[]
    def getData(self,name,age,id,m1,m2):
        Student.name=name
        Student.age=age
        Student.id=id
        Student.marks.append(m1)
        Student.marks.append(m2)
    def Display(self):
         print("student Name: ",Student.name)
         print("student age : ", Student.age)
         print("student id: ", Student.id )
         print("Marks are: ",Student.marks)
         print("Total Marks are: ",self.total())
    def total(self):
        return(self.marks[0]+self.marks[1])

name=input("enter the name: ")
age=int(input("enter the age: "))
id=int(input("enter the id: "))
m1=int(input("enter the marks m1: "))
m2=int(input("enter the marks m2: "))
s1=Student()
s1.getData(name,age,id,m1,m2)
print()
s1.Display()
