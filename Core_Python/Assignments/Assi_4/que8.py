#8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

n =int(input("enter the range number :"))

for i in range(1,n):
    if(i % 7 == 0 and i % 5 == 0):
        print("the number is both",i)