num=int(input('Enter the number : '))
temp=num
sum=0
while(num >0):
        num1= num %10
        num=num //10
        multi=1
        for i in range(1,num1+1):
            multi *=i
        sum +=multi
print(f'{sum} is sum of the every digit of number')

if(sum ==temp):
      print('the number is strong number')

else :
      print(f'{temp} is not strong number')