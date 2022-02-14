import array as arr
a=arr.array('i',[1,2,3])
print("The new created array is:",end=" ")
for i in range(0,3):
    print(a[i],end=" ")
print("\r")

b=arr.array('d',[1.2,3.4,4.5])
print("The new created array is:",end=" ")
for i in range(0,3):
    print(a[i],end=" ")
print("\r")


a.insert(1,4)
print("Array after inserting:",end=" ")
for i in (a):
    print(i,end=" ")
print("\r")

a=arr.array('i',[1,2,3,4,5]) #remove the value at the position of index
print(a.pop(2))
print("The array after popping is:",end=" ")
for i in range(0,4):
    print(a[i],end=" ")
print("\r")

a.remove(2)  #remove 1st occurence of 2
print("the array after removing is:",end=" ")
for i in range(0,3):
    print(a[i],end=" ")



