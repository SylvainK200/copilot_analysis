t=eval(input())
import sys
while t>0:
    t=t-1
    n=eval(input())
    a=list(map(int,input().split()))
    b=[0 for x in range(0,n+1)]
    b[n]=1
    i=n-1
    while i>=1:
        if (a[i]*a[i-1])<0:
            b[i]=b[i+1]+1
        else:
            b[i]=1
        i=i-1
    for i in range(1,len(b)):
        sys.stdout.write(str(b[i]))
        sys.stdout.write(" ")
    print("")