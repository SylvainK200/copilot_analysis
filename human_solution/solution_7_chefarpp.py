K=int(input())
ans=[]
for i in range(K):
    N=int(input())
    arr=list(map(int,input().split()))
    ct=0
    for j in range(N):
        k=j
        add=0
        prod=1
        while k<N:
            add=add+arr[k]
            prod=prod*arr[k]
            if add==prod:
                ct=ct+1
            k=k+1
    ans=ans+[ct]

for i in range(len(ans)):
    print(ans[i])
