def cal(n,k):
        r=0
        i=0
        num=list(map(int,input().split()))
        while(n!=0):
            temp=num[i]%k
            if(num[i]<k):
                r+=k-num[i]
            else:
                r+=min(temp,k-temp)
            #r+=min(temp,k-temp)
            i=i+1
            n=n-1
        print(r)
        
t=int(input(""))        
while(t!=0):
    n1=list(map(int,input().split()))
    cal(n1[0],n1[1])
    t=t-1