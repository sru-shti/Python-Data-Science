li=[10,34,45,34,576,783,324,63,35,56,6]
max=li[0]
smax=0

for ind in range(1,len(li)):
    if(li[ind] > max):
        smax=max
        max= li[ind]
    elif(li[ind] > smax):
        smax= li[ind]
print ('max :',max)
print ('smax :', smax)