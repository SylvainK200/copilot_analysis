t = eval(input())

while t:
    t -= 1
    n,m = list(map(int,input().split(" ")))
    arr = [int(x) for x in input().split()]
    minn = min(arr)
    maxx = max(arr)
    av = (minn+maxx)/2
    for i in range(0,av+1):
        print(maxx-i, end=' ')
    for i in range(av+1,n):
        print(i-minn, end=' ')
    print()