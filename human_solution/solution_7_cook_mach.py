import math
def check(n) :
    x = 2
    if n == 1 or n==2 :
        return True
    else :
        while(x <= n) :
            if x == n :
                return 1
                break
            x *= 2
    return 0
t=eval(input())
for i in range(t):
    n1,n2=list(map(int,input().split()))
    opr=0
    while(n1!=n2):
        if n1%2!=0 and n1!=1:
            n1=(n1-1)/2
            opr+=1
        else:
            flag=check(n1)
            if flag==0:
                n1=n1/2
                opr+=1
            else:
                if n1<n2:
                    n1=n1*2
                    opr+=1
                elif n1>n2:
                    n1=n1/2
                    opr+=1
                else:
                    pass
    print(opr)               
 