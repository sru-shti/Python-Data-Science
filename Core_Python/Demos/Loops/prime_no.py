num=int(input('enter the number :'))

if(num >1) :
    #for i in range(2,num):    => use only when the number is short like 7,8,9
    for i in range(2, num // 2 + 1):
        print(i)
        if(num % i ==0):
            print(f'{num} number is Not prime number')
            break
    else:
        print(f'{num} number is Prime number')
else:
    print(f'{num} number is Not prime number')