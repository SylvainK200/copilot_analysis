for asd in range(int(input())):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    mini=10000000000
    count=0
    for i in range (n):
        for j in range(i+1,n):
            temp=abs(a[j]+a[i]-k)
            if(temp==mini):
                count+=1
            elif (temp<mini):
                mini=temp
                count=0
    print(mini,count+1)
