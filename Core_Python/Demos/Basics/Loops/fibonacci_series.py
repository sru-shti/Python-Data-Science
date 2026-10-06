n=int(input('enter the number for fibonaaci series :'))
a=-1
b=1
#use end=" " parameter for num to appear in same line
for i in range (0,n):
    c=a+b
    print(c,end=' ')
    a=b
    b=c