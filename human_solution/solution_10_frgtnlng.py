T=eval(input())
for i in range(T):
    N,K=tuple(input().split())
    N=int(N)
    K=int(K)
    A1=[]
    A2=[]
    
    A1=input().split()

    for i in range(K):
        A2.append(input().split())

    for i in A1:
        c=0
        for j in range(len(A2)):
            if i in A2[j]:
                c=c+1
                break
        if c>=1:
            print("YES")
        if c==0:
            print("NO")
