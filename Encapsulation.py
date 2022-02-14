# #protected
class Vechile:
    def __init__(self):
        self._a= 2
class Car(Vechile):
    def __init__(self):
        Vechile. __init__(self)
        print("calling protected member of the base class: ",self._a)
        self._a=3
        print("calling modified protected member outside class: ",self._a)

obj1=Vechile()
obj2=Car()
print("Accessing protected member of obj1: ",obj1._a)
print("Accessing protected member of obj2: ",obj2._a)

#private
# class Base:
#     def __init__(self):
#         self._a="Lokesh"
#         self.__c="john"
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("calling private member of base class: ")
#         print(self.__c)
# obj1=Base()
# print(obj1._a)
# obj2=Derived()
# print(obj2.__c)