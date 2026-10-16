
def binary_sear(li,ele):
    beg=0
    end=len(li)-1
    while(beg <= end):

        mid=(beg + end)//2
        if( li[mid] == ele):
            return mid
        elif( ele < li[mid]):
            end = mid - 1
        elif(ele > li[mid]):
            beg = mid + 1
    else:
        return -1

li=[1,3,4,6,8,9,10,45,67]
ele=int (input("enter the element to find :"))
res=binary_sear(li,ele)
if(res != -1):
    print(f"the element {res} present in list")
else:
    print(f"the element {res} not present in list")
