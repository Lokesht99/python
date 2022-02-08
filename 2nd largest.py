num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
num3=int(input("enter thrid number: "))
if (num1>=num2) & (num1>=num3):
    if(num2>=num3):
        secondlargest=num2
    else:
        secondlargest=num3
elif (num2>=num1) & (num2>=num3):
    if(num1>=num3):
        seondlargest=num1
    else:
        secondlargest=num3
elif(num1>=num2):
    secondlargest=num1
else:
    secondlargest=num2
print("the 2nd largest ",secondlargest)