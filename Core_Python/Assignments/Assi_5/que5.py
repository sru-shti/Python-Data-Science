# 5. Write a program to print prime numbers between 1 to 100.

start=2
end=100
while start <= end:
    prime= True
    for i in range(2,start):
        if(start % i == 0):
            prime =False
            break
    if prime:
        print(start,end=" ")
    start +=1