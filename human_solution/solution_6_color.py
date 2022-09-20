T=int(input())
i=0
while(i<T):
    N=int(input())
    S=str(input())
    r=S.count('R')
    b=S.count('B')
    g=S.count('G')
    #print r,b,g
    maxi=max(r,b,g)
    #print maxi
    temp=N-maxi
    print(temp)
    i=i+1
