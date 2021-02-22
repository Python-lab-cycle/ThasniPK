print("print leap year between two given years")
print("enter the start year")
startYear=int(input())
print("enter the last year")
endYear=int(input())
print("list of leap years: ")
if(year%4==0) and (year%100!=0) or (year%400==0):
    print(year)
