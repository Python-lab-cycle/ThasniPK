#place the code in calculation.py
def summation(a,b):
    return a+b
def multiplication(a,b):
    return a*b
def divide(a,b):
    return a/b
from calculation import summation
 #it will import only the summation() from the calculation.py
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
print("sum=",summation(a,b))
#we do not need to specify the module name while accessing summation()
