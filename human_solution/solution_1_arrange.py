def deci2bin(n):
    bstr=''
    if n==0: return '0'
    while n>0:
        bstr= bstr + str(n%2)
        n=n>>1
    return bstr

def getindex(n,k):
    s1=deci2bin(n)
    t=k-len(s1)
    aps=''
    if t>0:
	    s1 = s1 + t*'0'
    return int(s1,2)

t= int(input())
for j in range(t):
    fip=input()
    lst=fip.split()
    k=int(lst[0])
    ip = lst[1]
    op=''
    for i in range(len(ip)):
        op=op+ip[getindex(i,k)]
    print(op)
    
