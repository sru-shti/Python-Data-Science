# write a program to reverse a number
def reverse(num):
    if (num ==0):
        return 0

    print(num % 10 ,end=' ')
    reverse(num=num // 10)
    

n=int(input('enter the number :'))
reverse(n)