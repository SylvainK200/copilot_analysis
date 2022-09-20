def gcd(a,b):
    while(b!=0):
        t=b
        b=a%b
        a=t
    return a

for _ in range(int(eval(input()))):
    n=int(eval(input()))
    arr=list(map(int,input().split()))
    ans=gcd(arr[0],arr[1])
    
    for i in range(2,n):
        ans=gcd(ans,arr[i])
    
    print(ans)