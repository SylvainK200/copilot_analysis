str=input()
l=len(str)
a=b=c=i=0
ans=0
while i<l:
    if str[i]=='C':
        a+=1
    elif str[i]=='H' and a>=1+b:
        b+=1
    elif str[i]=='E' and b>=1+c:
        c+=1
    elif str[i]=='F' and c>=1:
        a-=1
        b-=1
        c-=1
        ans+=1
    i+=1


print(ans)
    
