n=eval(input())
for i in range(n):
    t=eval(input())
    c=1
    a=list(map(int,input().split()))
    for j in range(0,t-1):
        if (a[j]>0 and a[j+1]>0) or (a[j]<0 and a[j+1]<0):
            for k in range(c,0,-1):
                print(k, end=' ')
            c=1
        else:
            c+=1
    for k in range(c, 0,-1):
        print(k, end=' ')
    print()