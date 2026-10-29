# 7. Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + .....n!

n=int(input("Enter the number :"))
total_fact=0

for i in range(1,n+1):
    fact = 1
    for j in range(1,i+1):
        fact *= j
    
    total_fact=total_fact + fact
print(total_fact)



# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

total_expo=0
for i in range(1,n+1):
    total_expo=total_expo + n**i
print(total_expo)

# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.

total_ratio=0
for i in range(0,n):
    total_ratio=total_ratio + 2**i
print(total_ratio)

# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
# e. x - x2/3 + x3/5 - x4/7 + .... to n terms

