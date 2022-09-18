a,b=list(map(int,input().split()))
array1=input()
array=[[0]*(a+1) for i in range(10)]
#print array
for i in range(10):
    for j in range(1,a+1):
        array[i][j]=array[i][j-1]
        if(int(array1[j-1])==i):
            array[i][j]+=1
#calculating B1
for k in range(b):
    b1=0
    b2=0
    x=int(input())
    x-=1
    #print int(array1[x])
    for i in range(int(array1[x])):
        #print (array[i][x])
        b1+=(array[i][x])*(int(array1[x])-i)
    for i in range(int(array1[x])+1,10):
        b2+=array[i][x]*(int(array1[x])-i)
    #print array
    #print b1, b2
    print(b1-b2)
