import itertools
for t in range(int(input())):
    n,m=list(map(int,input().split()))
    a=[]
    for i in range(n):
        a.append(int(input()))
    a.sort()
    s=[]
    for i in a:
        if i>m:
            break
        s.append(i)
    flag=0
    for i in range(1,len(s)+1):
        if flag==0:
            for w in itertools.combinations(s,i):
                if sum(w)==m:
                    flag=1
                    break
    if flag==1:
        print("Yes")
    else:
        print("No") 