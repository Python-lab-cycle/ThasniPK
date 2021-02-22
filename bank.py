class bank():
    def __init__(self,acnt,nam,typ,amt):
        self.ac=acnt
        self.name=nam
        self.type=typ
        self.amount=amt
    def printamt(self):
        print("acnt name",self.name)
        print("acnt num",self.ac)
        print("acnt type",self.type)
        print("bal=",self.amount)
    def with1(self,w1):
        return(self.amount-w1)
n=input("enter name")
t=input("enter type")
a=int(input("enter number:"))
am=int(input("enter amnt:"))
obj=bank(a,n,t,am)
print("account details")
obj.printamt()
w=int(input("enter amnt to withdraw"))
print("b1=",obj.with1(w))
