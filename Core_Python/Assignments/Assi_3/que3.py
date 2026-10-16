# Write a program to input angles of a triangle and check whether triangle is valid or not.

a=int(input('enter the first angle of triangle :'))
b=int(input('enter the second angle of triangle :'))
c=int(input('enter the third angle of triangle :'))

if(a+b+c == 180):
    print('the triangle is valid')
else:
    print('the triangle is not valid')