# 12. Write a program to check if given 3 digit number is a palindrome or not.

num=int(input("Enter the 3 digit number :"))

# num % 10 → 121 % 10 = 1 (gets the last digit).
# num // 100 → 121 // 100 = 1 (gets the first digit).

if(num>=100 and num<=999):
    last=num % 10
    first= num // 100

    if(last == first):
        print("the number is palindrome")
    else:
        print("the number is not palindrome")
else:
    print("plz enter the valid palindrome")