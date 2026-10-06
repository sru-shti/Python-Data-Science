num=int(input('enter the threee digit numbers :'))
d1=num%10
num=num //10

d2=num %10
num=num //10

d3=num %10
num=num //10

sum=d1 +d2 +d3
print('total sum of all digits' ,sum)