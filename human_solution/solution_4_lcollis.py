# cook your code here
ans=0
t=int(input())
for x in range(t):
    n,m=list(map(int,input().split()))
    l=[0]*m
    for i in range(n):
        a=list(map(int,input()))
        for j in range(m):
            l[j]+=a[j]
    ans=0;
    for i in range(m):
        ans+=(l[i]*(l[i]-1))/2
    print(ans)