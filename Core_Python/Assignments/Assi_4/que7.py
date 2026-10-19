#7. WAP to print all integers upto n that aren’t divisible by 2 and 3.

n=int(input("enter the n number :"))

for i in range(0,n):
    if(i  % 2 != 0 and  i % 3 !=0):
        print (i,end=" ")
     