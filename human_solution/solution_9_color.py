T=eval(input())
for i in range(0,T):
    N=eval(input())
    S=input()
    noR=S.count("R")
    noG=S.count("G")
    noB=S.count("B")
    ans=len(S)-max(noR,noG,noB)
    print(ans)
 
