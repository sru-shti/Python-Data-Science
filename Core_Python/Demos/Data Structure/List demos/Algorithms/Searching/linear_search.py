def linearSearch(li,search_ele):
    for ind in range(0,len(li)):
        if(search_ele == li[ind]):
            return ind
        else:
            return -1
li =[10,34,56,68,39,86,35,69,243]
search_ele = int(input("Enter the elemnt to be serched :"))
res=linearSearch(li,search_ele)

if(res != -1):
    print(f'{search_ele} is present at the index {res}')
else:
    print(f'{search_ele} is not present in list')