import sys
a =  int(input())
while a>0:
    s=input()
    i=l=c=0
    k=s.split("#")
    b=len(k)
    while i<b:
        j=k[i].count(".")
        if j>l:
            c+=1
            l=j
        i+=1
    print(c)
    a-=1
