T = eval(input())
for _ in range(T):
    n,m = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    s = min(arr)
    l = max(arr)
    for i in range(n):
        if abs(i-s)>abs(i-l):
            print(abs(i-s), end=' ')
        else:
            print(abs(i-l), end=' ')
