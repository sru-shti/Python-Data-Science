#10. WAP to check if given number is Perfect Number.

# perfect no - A perfect number is a number that is equal to the sum of its proper factors (all positive factors except the number itself).
# Factors of 28, excluding 28 itself:
# (1 + 2 + 4 + 7 + 14 = 28)   ==> So, 28 is a perfect number.
# Factors of 10, excluding 10 itself:
# (1 + 2 + 5 = 8)            ==>  Since  10 is not a perfect number.

n=int(input("enter the n number :"))
fact=0
for i in range(1,n):
    if( n % i == 0):
        fact += i
if(fact == n):
            print("the number is perfect num :",fact)
else:
            print("the number is not perfect num :",n)

