def gcd(a,b):
    if b<a:
        a,b = b,a
    while a is not 0:
        r=b%a
        b,a = a,r
    return b
def show(l):
    g=l[0]
    for i in l:
        g=gcd(g,i)
    return g

t=int(input())
while(t>0):
    n=int(input())
    l=[int(i) for i in input().split()]
    g=show(l)
    print(g)
    t-=1
