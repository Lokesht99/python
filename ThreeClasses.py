# #multi level inheritance
#
# class Employee():
#     def func1(self,ename, eid,esal):
#         self.ename=ename
#         self.eid=eid
#         self.esal=esal
#     def displayEmployee(self):
#         print(f"name : {self.ename} id:{self.eid} sal:{self.esal}")
# class Department():
#     def func2(self,dname,did,dcourse):
#         self.dname=dname
#         self.did=did
#         self.dcourse=dcourse
#     def displaydepartment(self):
#         print(f"dept name : {self.dname} dept id:{self.did} dept course:{self.dcourse}")
# class Admin(Employee,Department):
#     def __init__(self):
#         self.name="Admin"
#
# a=Admin()
# a.func1("john",100,200000)
# a.func2("mca",101,"python")
# a.displayEmployee()
# a.displaydepartment()
#
# --------------------------------------------------------------

class DefaultConstructor:
    def __init__(self):
        self.name="default"
        print("default constructor : ",self.name)
class ParamConstructor:
    def __init__(self,name):
        self.name=name
    def __del__(self):
        print("deleted......")

    def display(self):
        print(f"parametraised constructor : {self.name}")

c=DefaultConstructor()
p=ParamConstructor("john")
p.display()