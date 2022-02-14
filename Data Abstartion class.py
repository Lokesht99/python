# from abc import ABC
# class Car(abc.ABC):
#     def mileage(self):
#         pass
# class Tesla(Car):
#     def mileage(self):
#         print("The mileage is 30kmph")
# class Suzuki(Car):
#     def mileage(self):
#         print("The mileage is 20kmph ")
# class Safari(Car):
#     def mileage(self):
#         print("The mileage is 35kmph ")
# t=Tesla()
# t.mileage()
# s=Suzuki()
# s.mileage()
# s1=Safari()
# s1.mileage()
# ----------------------------------------
import abc #abstract base class
#class Shape(metaclass=abc.ABCMeta): #ABCMeta Class
class Shape(abc.ABC): #ABC helper class
   # @abc.abstractmethod
   def area(self): #Abstract Method Declaration
      pass
class Rectangle(Shape):
   def __init__(self, x,y):
      self.l = x
      self.b=y
   def area(self):
      return self.l*self.b
r = Rectangle(10,20)
print ('area: ',r.area())
