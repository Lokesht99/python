class Dog:

   # class attribute
   a='Boy'
   # Instance attribute
   def __init__(self, name): #DEFAULT CONSTRUCTOR
      self.name = name
     # self.attr1 = "Boy"
      #print(self.attr1)

   def speak(self):
      print("My name is {}".format(self.name))
     # print(self.attr1)

# Driver code
# Object instantiation #DOG D("JANCY");
J = Dog("JANCY")  #SELF-->REPRESNTS THE INSTANCE
T = Dog("Tom")

# # Accessing class attributes
print("John is a {}".format(J.__class__.a))
print("Tom is also a {}".format(T.__class__.a))
#
# # Accessing instance attributes
print("My name is {} ... How are you  {}".format(J.name,J.name))
print("My name is {}".format(T.name))

# Accessing class methods
J.speak()
T.speak()