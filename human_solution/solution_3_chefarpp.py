def product(arr):
    mul=1
    for i in arr:
        mul*=i
    return mul
for t in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=len(arr)
    for i in range(n):
        for j in range(i+2,n+1):
            if sum(arr[i:j])==product(arr[i:j]):
                ans+=1
    print(ans)
