from calcpackage.calcfunction import*
while True:
    print("select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")
    choice=input("enter your choice:")
    num1=int(input("enter first number:"))
    num2=int(input("enter second number:"))
    

    if choice =='1':
        print(num1,"+",num2,"=",addition(num1,num2))

    elif choice =='2':
        print(num1,"-",num2,"=",subtraction(num1,num2))

    elif choice =='3':
        print(num1,"*",num2,"=",multiplication(num1,num2))

    elif choice =='4':
        print(num1,"/",num2,"=",division(num1,num2))

    else:
        print("invalid choice")
        break
