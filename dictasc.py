d={1:2,3:4,4:3,2:1,0:0}
print('original dictionary:',d)
sorted_d=sorted(d.items())
print('dictionary in ascending order by value:',sorted_d)
sorted_d=sorted(d.items(),reverse=True)
print('dictionary in descending order by value :',sorted_d)
