import module
import csv
class Employee:
    def employeeDetails(self):
        with open('C:\pandascsvfiles\data.csv','r', newline='') as csvfile:
            data = csv.reader(csvfile, delimiter='\t', quotechar='|')
            for row in data:
                print(','.join(row))
class Department(Employee):
    def departmentDetails(self):
        super()
        with open('C:\pandascsvfiles\department.csv', newline='') as csvfile:
            data = csv.reader(csvfile, delimiter='\t', quotechar='|')
            for row in data:
                print(','.join(row))
# object of Manager class
obj = Department()
# output
print("-----Employee Detail-----")
obj.employeeDetails()
print("-----Department Detail-----")
obj.departmentDetails()



