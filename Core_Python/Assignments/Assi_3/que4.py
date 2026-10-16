# Write a program to input all sides of a triangle and check whether triangle is valid or not.
# NOTE :A triangle is valid if the sum of any two sides is greater than the third side:

s1=int(input('Enter the first side of triangle :'))
s2=int(input('Enter the second side of triangle :'))
s3=int(input('Enter the third side of triangle :'))

if(s1+s2 > s3 or s2+s3 >s1 or s3+s1 >s2):
    print('the triangle is valid')
else:
    print('the triangle is not valid')