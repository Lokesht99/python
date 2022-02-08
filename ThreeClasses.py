class Employee():
    def func1(self,ename, eid):
        self.ename=ename
        self.eid=eid
    def displayEmployee(self):
        print(f"name : {self.ename} id:{self.eid}")
class Department():
    def func2(self,dname,did):
        self.dname=dname
        self.did=did
    def displaydepartment(self):
        print(f"dept name : {self.dname} dept id:{self.did}")
class Admin(Employee,Department):
    def __init__(self):
        self.name="Admin"

a=Admin()
a.func1("john",100)
a.func2("mca",101)
a.displayEmployee()
a.displaydepartment()
