#3. WAP to print sum of series upto n.

n=int(input("enter the n number :"))
sum=0
for i in range (1,n+1): # 1,2,3,4,5,6,7,8,9,10  => for 1 to 10( 1,11)
    sum += i
print(sum)