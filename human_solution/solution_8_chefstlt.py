# cook your code here

t=int(input())
for i in range(t):
    s1=input()
    s2=input()
    
    count=0 #count of '?'
    min=0   #minimal diff.
    for j in range(len(s1)):
        if s1[j]=='?' or s2[j]=='?':
            count+=1
        else:
            if s1[j]!=s2[j]:
                min+=1
                
    max=min+count   #maximal diff.
    
    print(min, max)