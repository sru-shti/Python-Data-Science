#6. WAP to check if a given number is prime number or not.

n=int(input("enter the n number :"))

if (n <=1):
    print("Not a prime number ")
else:
    for i in range(2,n):
        if(n % i ==0):
            print("the number is is not prime number")
            break
    else:
            print("the number is prime number")