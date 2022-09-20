t=int(input())
for i in range(t):
    n,y=list(map(int,input().split()))
    x=list(map(int,input().split()))
    x.sort()
    counter=0
    mini=20000000000
    for j in range(n):
        for k in range(j+1,n):
            if abs(x[j]+x[k]-y)<mini:
                mini=abs(x[j]+x[k]-y)
                counter=1
            elif abs(x[j]+x[k]-y)==mini:
                counter+=1
    print(mini,counter) 