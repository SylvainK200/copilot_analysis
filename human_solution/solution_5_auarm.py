t=int(input())
for asd in range(t):
    n,m=list(map(int,input().split()))
    a=list(map(int,input().split()))
    s1=0
    s2=0
    for i in a:
        s1=max(i,s1)
        s2=max(n-1-i,s2)
    b=[0]*n
    b[0]=s1
    b[n-1]=s2
    for i in range(1,n-1):
        b[i]=max(s1-i,s2-(n-i-1))
    for i in b:
        print(i, end=' ')
    print(" ")
        
