import csv
with open('Emp.csv',newline='')as csvfile1:
    data=csv.DictReader(csvfile1)
    print("empno empname")
    print("--------------------")
    for i in data:
        print(i['empno'],i['empname'])
