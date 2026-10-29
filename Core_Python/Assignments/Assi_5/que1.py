# 1. Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.

corr_username="Admin123"
corr_password="12345"

count=1
while(count <=3):
    username =input("Enter the username : ")
    passw=input("enter the password :")

    if(username == corr_username or passw == corr_password):
        print("the signin is succe3sfull")
    else:
        print("Wrong credentisals")
        count+=1

if(count>3):
    print("you have exhaust 3 chances")
    