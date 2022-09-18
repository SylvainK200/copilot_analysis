n,m=input().split()
n=int(n)
m=int(m)
digs=list(str(input()))
sums=[]
tmp=0
mapp=[]
for i in range(0,10):
    if ord(digs[0])-48==i:
	mapp.append([1])
    else:
	mapp.append([0])
for i in range(1,n):
    for j in range(0,10):
	if ord(digs[i])-48==j:
	    mapp[j].append(mapp[j][i-1]+1)
	else:
	    mapp[j].append(mapp[j][i-1])
for i in range(0,m):
    ind=int(input())
    ind-=1
    ans=0
    if ind>0:
	ul=int(digs[ind])
	for j in range(0,10):
	    if j<=ul:
		ans+=(ul-j)*mapp[j][ind]
	    else:
		ans+=(j-ul)*mapp[j][ind]
    print(ans)
	