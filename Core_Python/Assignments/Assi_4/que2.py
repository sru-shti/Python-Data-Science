#2. WAP to print all odd numbers until n.

n=int(input("enter the n number :"))

for i in range (0,n):
    if(i % 2 ==1):
        print(i)