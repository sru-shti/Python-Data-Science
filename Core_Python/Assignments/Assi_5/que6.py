# 6. Write a program to print first n prime numbers.

n=int(input("enter how many prime numbers :"))
start=2
count=0
while count < n:
    prime= True
    for i in range(2,start):
        if(start % i == 0):
            prime =False
            break
    if prime:
        print(start,end=" ")
        count+=1
    start +=1