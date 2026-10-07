# 1. To pass multiple value parameters in function
# 2. Mention 1 asterisk before para name in fuction defination
# 3. VAlues are stored in tuple format
# 4. Use for loop for oterate over values in tupleindividully

def add(*data):
    sum=0
    for val in data:
        sum +=val
    return sum

res=add(1,2,3,4,5,6,7,8,8,9,0,3,35,43,64)
print(res)