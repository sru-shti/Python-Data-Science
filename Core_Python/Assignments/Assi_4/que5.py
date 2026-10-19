#5. WAP to print Fibonacci series upto n.

n=int(input("enter the n number :"))
a=-1
b=1
for i in range(0,n):
    c = a + b
    print(c,end=" ")
    a = b
    b = c

