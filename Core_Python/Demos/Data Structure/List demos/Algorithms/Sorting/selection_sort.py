
def selectionSort(li):
    size=len(li)
    for i in range(0,size-1):
        min_idx=i
        for j in range(i+1 ,size):
            if(li[j] > li[min_idx]):
                min_idx =j
        li[i] , li[min_idx] = li[min_idx] ,li[i]

li=[2,5,34,12,86,4,6]
print("before sorting :", li)
selectionSort(li)
print("After sorting :",li)