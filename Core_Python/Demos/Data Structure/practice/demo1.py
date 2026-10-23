path=input("Enter the path in the form of E,W,N,S : ")
x=0
y=0
for pos in path:
    if(pos == 'N'):
        y+=1
    elif(pos == 'S'):
        y-=1
    elif(pos == 'E'):
        x+=1
    elif(pos == 'W'):
        x-=1
    else:
        print('Invalid path')
        break
else:
    dist=((x ** 2)+(y ** 2))** 0.5
    print(f'Shortest distance of your path is :{dist}')