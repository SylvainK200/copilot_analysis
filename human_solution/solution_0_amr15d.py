# cook your code here
from math import *
n=eval(input())
a=list(map(int,input().split()))
a=sorted(a)
c=[a[0]]
for i in range(1,n):
    c.append(c[i-1]+a[i])
for _ in range(eval(input())):
    k=eval(input())
    q=int(ceil(n/float(k+1)))
    print(c[q-1])