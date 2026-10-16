# Write a program to check if user has entered correct userid and password.

userId=input('enter the userid of person :')
password=input('enter the password only in numerically format in 6-7 number :')

if(userId == 'adm8in' and password =='1234567'):
    print('correct userid and password')
else:
    print('incorrect userid and password')