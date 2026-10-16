# Input 5 subject marks from user and display grade(eg.First class,Second class ..)

math=int(input('enter the marks of math :'))
eng=int(input('enter the marks of english :'))
geo=int(input('enter the marks of geography :'))
phy=int(input('enter the marks of physics :'))
chem=int(input('enter the marks of chemistry :'))

sum=math +eng + geo + phy + chem
if(sum >=75):
    print('get first class in exam')
elif(sum >=50):
    print('get second class in exam')
elif(sum >=25):
    print('get third class in exam')
else:
    print('Failed in exam')