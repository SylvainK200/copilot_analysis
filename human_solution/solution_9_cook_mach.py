for t in range(int(input())):
    a,b=list(map(int,input().split()))
    c=0
    while (a&-a)!=a:
        a>>=1
        c+=1
    while a<b:
        a<<=1
        c+=1
    while a>b:
        a>>=1
        c+=1
    print(c)
    
        
