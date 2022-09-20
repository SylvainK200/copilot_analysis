for _ in range(eval(input())):
    s1=input()
    s2=input()
    minl=0
    maxl=0
    for i in range(len(s1)):
        if s1[i]=='?' or s2[i]=='?':
            x=0
        elif s1[i]!=s2[i]:
            minl+=1

    for i in range(len(s1)):
        if s1[i]!=s2[i] or (s1[i]=="?" and s2[i]=="?"):
            maxl+=1
    print(minl,maxl)
