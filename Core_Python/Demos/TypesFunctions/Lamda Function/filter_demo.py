data =[1,2,3,4,5,6,7,8,9,10]
res= list(filter(lambda n: n*n ,data))
print(res)

data =[1,2,3,4,5,6,7,8,9,10]
res= list(filter(lambda n: n % 2 ==0 ,data))
print(res)