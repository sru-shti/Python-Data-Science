# write a program to cal factorial using recursive function
# 5! = 5 X 4 x 3 x 2 x 1 = 120

def fact(n):
    if(n <=1):
        return 1
    else:
        return n * fact(n-1)
n=int(input('enter the fact number :'))
res=fact(n)
print(res)
