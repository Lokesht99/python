#using default arguments

# class Calculate:
#     def sub(self,a,b,c=0):
#         if c>0:
#             print("a-b-c={}".format(a-b-c))
#         else:
#             print("a-b={}".format(a-b))
# c1=Calculate()
# c1.sub(20,5,7)
# c1.sub(10,20)

#using variable length arguments

class Calculate:
    def add(self, *arg):
        result=0
        for param in arg:
            result=result + param
            print("result: {}".format(result))
c1=Calculate()
c1.add(10,20,30,40)
c1.add(10,20)