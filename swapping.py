str1=input("enter a first string:")
str2=input("enter a second string:")
new_a=str2[:2]+str1[2:]
new_b=str1[:2]+str1[2:]
print("the new string after swapping first 2 chraracters of both strings:",(new_b+' '+new_a))
