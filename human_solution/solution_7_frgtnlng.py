for i in range(int(input())):
    a=list(map(int,input().split()))
    b=input().split()
    c=[]
    for j in range(a[1]):
        c.append([])
        c[j]=input().split()
    for j in range(a[0]):
        f=0
        for k in range(a[1]):
            if b[j] in c[k]:
                f=1
                break;
        if f==1:
            print("YES", end=' ')
        else:
            print("NO", end=' ')
    print()