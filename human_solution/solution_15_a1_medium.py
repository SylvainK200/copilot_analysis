import itertools
def prnt(a,n,m):
    if m==0:
        return True
    if n==0:
        return False
    if a[n-1]>m:
        return prnt(a,n-1,m)
    else:
        return prnt(a,n-1,m-a[n-1]) or prnt(a,n-1,m)

t=int(input())
while t>0:
    t-=1
    a=[]
    [n,m]=list(map(int,input().split()))
    i=0
    while i<n:
        a.append(int(eval(input())))
        i+=1
    if prnt(a,n,m):
        print("Yes")
    else:
        print("No")
    
