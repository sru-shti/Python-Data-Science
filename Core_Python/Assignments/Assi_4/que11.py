#11. WAP to check if given number Strong Number.
# number whose sum of the factorials of its individual digits is equal to the original number.
# 145 - Strong Number 
# (1! + 4! + 5! = 1 + 24 + 120 = 145)
# 123 -Not a Strong Number
# (1! + 2! + 3! = 1 + 2 + 6 = 9)

n=int(input("enter the n number :"))
temp=n
sum=0
while(n> 0):
    fact=1
    n1 = n % 10
    for i in range(1,n1 + 1 ):
        fact=fact * i
       #print(f"factorial of {n1} is {fact} ")
    print(f"factorial of {n1} is {fact} ")
    sum = sum + fact
    print("sum is :",sum)
    n = n // 10

if(sum == temp):
    print("is a strong nummber")
else:
    print("is not a strong nummber")