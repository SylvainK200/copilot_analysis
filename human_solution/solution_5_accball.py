import sys
t=int(input(""))
while t:
    x=str(input(""))
    y=str(input(""))
    l=""
    for i in range(len(x)):
        if x[i]!=y[i]:
            l+="B"
        elif x[i]==y[i] and x[i]=="B":
            l+="W"
        else:
            l+="B"
    print(l)
    t-=1
