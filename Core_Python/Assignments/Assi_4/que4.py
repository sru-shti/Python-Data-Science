#4. WAP to print factorial of a number

num=int(input("enter the n number :"))
fact=1
for i in range(1,num+1):
    fact *= i
    print(fact,end=" ")
print()
print("the factorial is :",fact)




# THIS ARE FACTORS OF NUMBERS NOT FACTORIAL 

# for i in range(1,num+1):
#     if(num % i == 0):
#         print(i,end =" ")