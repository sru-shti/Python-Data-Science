# write a program to seprate digit from a numbers

def sep_digit(num):
    if (num ==0):
        return 0
    
    sep_digit(num=num // 10)
    print(num % 10 ,end=' ')

n=int(input('enter the number :'))
sep_digit(n)