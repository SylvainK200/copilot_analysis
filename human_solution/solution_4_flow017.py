for i in range(int(input())):
    a=list(map(int,input().split()))
    a.sort()
    if a[1]!=max(a):
        print(a[1])
    else:
        print(a[2])