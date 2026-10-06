# write a program to cal sum of digits in a numbers

def sumOfDigit(num):
    if(num ==0):
        return 0
    num1 =num %10
    num= num //10
    return sumOfDigit(num) + num1

n=int(input('enter the number :'))
res=sumOfDigit(n)
print(res)