for tc in range(int(input())):
    s=input()
    d=input()
    mi=0
    ma=0
    for i in range(len(s)):
        if(s[i]=='?' or d[i]=='?'):
            ma+=1
            continue
        if s[i]!=d[i]:
            mi+=1
    print(str(mi)+" "+str(mi+ma))
