def bubble(li):
    size=len(li)
    for i in range  (1,size):
        for j in range (0,size-i):
            if(li[j] > li[j + 1]):
                li[j] ,li[j+1] = li[j+1] ,li[ j] # swap method
                print(li)

li=[2,7,6,3,1,9,32]
print("Before sorting :",li)
bubble(li)
print("After sorting :",li )