# Write a program to prompt user to enter userid and password. After verifying userid and password display a 4 digit
# random number and ask user to enter the same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)


import random
userId=input('enter the userid of person :')
password=input('enter the password only in numerically format in 6-7 number :')

if(userId == 'adm8in' and password =='1234567'):
    num = random.randint(1000, 9999)
    # num=12345
    print(num)
    user_cap=int(input('enter the capcha number :'))
    if(user_cap == num):
        print('success')
    else:
        print('failed')
else:
    print('incorrect userid and password')