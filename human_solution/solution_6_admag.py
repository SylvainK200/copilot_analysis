def find(a,n):
    i=0
    while(a[i]<=n):
        i+=1
    return i-1

t=int(input())
i=2
a=[1,1]
while(i<100):
   a.append(a[i-1]+a[i-2])
   i+=1
while(t>0):
    n=int(input())
    t-=1
    print(find(a,n))
