for i in range(int(input())):
    a=list(map(int,input().split()))
    max=0
    for j in range(2,a[1]+1):
        if (a[0]-(a[0]/j)*j)>max:
            max=(a[0]-(a[0]/j)*j)
    print(max)