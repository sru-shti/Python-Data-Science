li=[10,20,30,40,50,6,99,23]
# max=0
# for ind in range(0,len(li)):
max=li[0]
for ind in range(1,len(li)):
    if(max< li[ind]):
        max =li[ind]
print(max)