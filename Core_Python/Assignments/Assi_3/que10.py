# Write a program to check if person is eligible to marry or not (male age >=21 andfemale age>=18)

age=int(input("enter the age of a person :"))
gender=input(" Enter the gender of the persong  {M/F}: ")

if(gender =='F'):
    if(age >=18):
        print("the female should be eligible for marrige")
    else:
        print("the female should wait for eligibility")
else:
    if(age >=21):
        print("the male should be eligible for marrige")
    else:
        print("the male should wait for eligibility")