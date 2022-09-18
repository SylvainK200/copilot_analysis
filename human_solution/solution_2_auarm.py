t=eval(input())
for _ in range(t):
    n,m=list(map(int,input().split()))
    m1=list(map(int,input().split()))
    min1=min(m1)
    max1=max(m1)
    mid=(min1+max1)/2
    for i in range(mid+1):
        print(max1-i, end=' ')
    
    for i in range(mid+1,n):
        print(i-min1, end=' ')
        
        
