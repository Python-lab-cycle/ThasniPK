import csv
csv_col=['ID','Name','Country']
dict_data=[{'ID':1,'Name':'Alex','Country':'India'},{'ID':2,'Name':'Aleena','Country':'India'},{'ID':3,'Name':'Jabbar','Country':'USA'},{'ID':4,'Name':'Afla','Country':'USA'},{'ID':5,'Name':'Thasni','Country':'India'},{'ID':6,'Name':'Haseena','Country':'australia'},{'ID':7,'Name':'Ashitha','Country':'Canada'},{'ID':8,'Name':'Anu','Country':'USA'},{'ID':9,'Name':'Alan','Country':'Canada'},{'ID':10,'Name':'Alexander','Country':'USA'}]
csv_file="Names.csv"
try:
    with open(csv_file,'w')as file1:
        writer=csv.DictWriter(file1,fieldnames=csv_col)
        writer.writeheader()
        for data1 in dict_data:
            writer.writerow(data1)
except IOError:
    print("I/O error")
data1=csv.DictReader(open(csv_file))
print("CSV file as a dictionary:\n")
for row in data1:
    print(row)
