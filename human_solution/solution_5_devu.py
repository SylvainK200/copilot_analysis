t=eval(input())
for i in range(t):
    n,k=list(map(int,input().split()))
    buck=list(map(int,input().split()))
    ng=0
    for j in buck:
        mod=j%k
        if(j<k):
            ng=ng+k-j
        else:
            ng=ng+min(mod,k-mod)
    print(ng)        

