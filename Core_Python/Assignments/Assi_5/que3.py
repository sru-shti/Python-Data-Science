# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

num = int(input("Enter number of passenger :"))
tk_cost=int(input("Enter the cost of ticket :"))
total_amount=0

for i in range(1,num):
    discount=0
    age=int(input("Enter the age of passenger :"))
    if(age <12):
        discount=tk_cost *30 //100
        dis_price= tk_cost - discount
    elif(age >59 ):
        discount=tk_cost *50 //100
        dis_price= tk_cost - discount
    else:
        dis_price=tk_cost

    total_amount += dis_price
print("total amount for all passenger is :",total_amount)