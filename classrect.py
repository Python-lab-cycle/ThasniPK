class rectangle():
    def __init__(self,breadth,length):
        self.breadth1=breadth
        self.length1=length
    def area(self):
        return self.breadth1*self.length1
a=int(input("Enter length of rectangle: "))
b=int(input("Enter breadth of rectangle: "))
obj=rectangle(a,b)
print("Area of rectangle:",obj.area())

#print()
                    
