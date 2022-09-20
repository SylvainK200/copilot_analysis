def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

t=eval(input())
while t>0:
    t=t-1
    n=eval(input())
    a=list(map(int,input().split()))
    g=a[0]
    for i in range(1,n):
        g=gcd(a[i],g)
    print(g)
    
