t=eval(input())
while(t>0):
    st=input()
    prev=0
    k=0
    w=0
    if(st[0]=='#' and st[len(st)-1]=='#'):
     for i in st:
        if(i=='.'):
            k+=1
        elif(i=='#'):
            if(k>prev):
                prev=k
                w+=1
            k=0
    print(w)
    t-=1
