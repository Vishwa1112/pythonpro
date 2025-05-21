def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
a=int(input("enter  number"))
b=int(input("enter a number"))    
print("choose your option")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
choice=int(input("enter your choice "))
if choice==1:
    print("addition ",add(a,b))
elif choice==2:
    print("subtraction",subtract(a,b))
elif choice==3:
    print("multiplication",multiply(a,b))
elif choice==4:
    print("dvision",divide(a,b))