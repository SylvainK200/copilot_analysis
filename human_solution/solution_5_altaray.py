t=eval(input())
ans=[]
for i in range(t):
    n=eval(input())
    s=input()
    s=s.split()
    tmp=[]
    tmp.append('1')
    flag=0
    if int(s[len(s)-1])<0:
        flag=0
    else:
        flag=1
    k=0
    for j in range(len(s)-2, -1, -1):
        if int(s[j])<0 and flag==1:
            a=2+int(tmp[k])-1
            tmp.append(str(a))
            k+=1
            flag=0
            continue
        if int(s[j])>=0 and flag==0:
            a=2+int(tmp[k])-1
            tmp.append(str(a))
            k+=1
            flag=1
            continue
        tmp.append('1')
        k+=1
    tmp.reverse()
    s=' '.join(tmp)
    s=s.strip()
    ans.append(s)
for i in range(t):
    print(ans[i])
