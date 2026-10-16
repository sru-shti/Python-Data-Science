# Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

a1=int(input('Enter the first side of triangle :'))
a2=int(input('Enter the second side of triangle :'))
a3=int(input('Enter the third side of triangle :'))

if(a1==a2==a3 ):
    print('triangle is equilateral triangle')
elif(a1==a2 or a2==a3 or a3==a1 ):
    print('the triangle is isoscale ')
else:
    print('triangle is scalene')
