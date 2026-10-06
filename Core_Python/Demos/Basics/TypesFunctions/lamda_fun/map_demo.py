# # 1 . To reduce line of code
# # 2 . Perform same task  multiple time on diff inputs 

def square(m):
    return m*m

data=[ 1,2,3,4,5,6,7,8,9,10]
res=list(map(square,data))
print(res)
# output -> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# METHOD -2

res=list(map(lambda m : m*m ,data))
print(res)


# output -> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
