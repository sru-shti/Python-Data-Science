gender=input('enter the gender (F/M) :')
age= int(input('enter the age :' ))

if(gender =='M'):
    if(age >=21):
        print('the boy is eiligible for marriage')
    else:
        print('pehele kama le')
else:
    if(age >=18):
        print('the girl is eligible for marriage')
    else:
        print('pehele padh le')