# 2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

n=int(input("Enter the number of student :"))
count=n
avg_total=0
while(n>0):
    total=0
    sub1=int(input("enter the marks of first subject : "))
    sub2=int(input("enter the marks of second subject : "))
    sub3=int(input("enter the marks of third subject : "))
    sub4=int(input("enter the marks of fourth subject : "))
    sub5=int(input("enter the marks of fifth subject : "))

    total= sub1 + sub2 + sub3 + sub4 + sub5
    perc= total/500 * 100
    print(f"Individual percentage of student :{perc} %")
    avg_total=avg_total + perc
    n=n-1

avg_perc= avg_total/count
print(f"Average percentage of students :{avg_perc} %")


