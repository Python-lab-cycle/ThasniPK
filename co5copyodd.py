fn=open('test1.txt','r')
fn1=open('odd.txt','w')
content=fn.readlines()
print("Content\n",content)
for i in range(0,len(content)):
    if(i%2==0):
        fn1.write(content[i])
    else:
        pass
fn1.close()
fn1=open('odd.txt','r')
cont1=fn1.read()
print("\n\n odd lines\n\n",cont1)
fn.close()
fn1.close()

