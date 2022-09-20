def gcd(a,b):
    if a>b:
        a,b=b,a
    while b>0:
        a,b=b,a%b
    return a
def gcdl(l):
    g=gcd(l[0],l[1])
    for i in range(2,n):
        g=gcd(g,l[i])
    return g
x=eval(input())
for i in range(x):
    n=eval(input())
    l=list(map(int,input().split()))
    print(gcdl(l))
        
