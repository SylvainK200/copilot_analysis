m=0
a=input()
for i in range(0,len(a)):
    c=0
    b=[]
    #print a[i]
    for j in range(i,len(a)):
        if a[j]>='A'and a[j]<='Z':
            c+=1
        if c>1:
                break
        else:
                b.append(a[j])

    for k in range(0,len(b)):
        if b[k]>='A'and b[k]<='Z':
            b[k]='9'
    #print b
    n=0
    for k in range(0,len(b)):
        n = (n<< 3) + (n<< 1) + int(b[k])
    if n>m:
        m=n
print(m)
