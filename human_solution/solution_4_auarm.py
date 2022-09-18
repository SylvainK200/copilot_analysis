T=int(input())
for i in range(T):
    N,r=list(map(int,input().split()))
    M=list(map(int,input().split()))
    a=min(M)
    b=max(M)
    for i in range(N):
        l=max(abs(b-i),abs(a-i))
        print(l, end=' ')
    print('')