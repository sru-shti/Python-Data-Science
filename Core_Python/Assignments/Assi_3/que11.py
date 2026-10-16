# Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

total_Amt=0
for i in range (1,6):
    age=int(input("enter the age of a person :"))
    ticket_Amt=int(input("enter the ticket amount of the person :"))
    discount_amt=0
    if(age <=12 ):
        discount_amt=ticket_Amt * 30 //100
        total_Amt += ticket_Amt-discount_amt
    elif(age >= 59):
        discount_amt=ticket_Amt * 50 //100
        total_Amt += ticket_Amt-discount_amt
    else:
        total_Amt += ticket_Amt
print(total_Amt)

