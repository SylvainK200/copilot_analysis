s=input()
l=len(s)
maxm=0
ans=[]
for i in range(l):
    j=i
    cnt=0
    k=0
   
    while(cnt<2 and j<l):
        p=s[j]
        
        if(p.isalpha()):
            cnt=cnt+1
        ans.append(s[j])
        j=j+1
    k=len(ans)
    
    if(cnt==0 or cnt==1):
        k=k-1
    else:
        k=k-2
    num=0
    for j in range(k+1):
        p=ans[j]
        if(p.isalpha()):
            ans[j]='9'
        dig=ord(ans[j])-48
        num=num*10+dig
    del ans[:]
    if(num>maxm):
        maxm=num
print(maxm)
 