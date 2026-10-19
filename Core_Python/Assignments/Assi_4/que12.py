# 12. Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
# 4*4*4*4)

n =int(input( " Enter the digit :"))
temp=n
count =0
while( n > 0):
    n = n // 10
    count += 1
print(count)

n=temp
total = 0
while (temp >0):
    n1=temp % 10 
    total = total + n1**count
    temp=temp // 10
print(total)

if (total ==n) :
    print("Armstrong number")
else:
    print("Not an Armstrong number")
