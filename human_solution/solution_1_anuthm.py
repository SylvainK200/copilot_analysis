test=eval(input())
while test:
    test-=1
    n,m=list(map(int,input().split()))
    print("%.6f"%(n+m-1))