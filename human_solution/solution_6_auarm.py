for t in range(int(input())):
    n,m=list(map(int,input().split()))
    a=list(map(int,input().split()))
    s=min(a)
    l=max(a)
    for i in range(n):
        if abs(i-s)>abs(i-l):
            print(abs(i-s), end=' ')
        else:
            print(abs(i-l), end=' ')
 