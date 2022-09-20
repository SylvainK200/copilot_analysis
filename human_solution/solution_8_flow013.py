t=int(input())
while t>0:
    t=t-1
    a,b,c = list(map(int,input().split()))
    k= a+b+c

    if k==180 and a>0 and b>0 and c>0:
        print("YES")
    else:
        print("NO")