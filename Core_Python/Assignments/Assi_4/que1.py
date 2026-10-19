#1. WAP to print all even numbers until n.

n=int(input("enter the n number :"))

for i in range (0,n):  # range from 0 to n-1 actually 
    if(i % 2 ==0):
        print(i)
