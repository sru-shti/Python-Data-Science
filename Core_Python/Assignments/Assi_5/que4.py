# 4. WAP to print Armstrong number within a given range

# 153 → \(1^3 + 5^3 + 3^3 = 153\) ✅ Armstrong number
# 123 → \(1^3 + 2^3 + 3^3 = 36\) ❌ Not an Armstrong number
# 1634 → \(1^4 + 6^4 + 3^4 + 4^4 = 1634\) ✅ Armstrong number

n=int(input("enter the number :"))
temp=n
count=0
total=0

while n>0:
    count +=1
    n=n //10

n=temp
while n>0:
    digit=n %10
    total=total +digit**count
    n= n//10

if total ==temp:
    print("is armstrong num")
else:
    print("is not an armstrong num")