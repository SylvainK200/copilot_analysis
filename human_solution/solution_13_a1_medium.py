def check(a,m):
	if (len(a)>0 and  m<a[-1]):
		return 0
	else:
		pos=0
		while (m<a[pos]):
			pos+=1
		m=m-a[pos]
		b=a[pos+1:]
		while (1):
			if (m==0):
				return 1
			if (len(b)<=0):
				return 0
			if(check(b,m) and pos<len(a)):
				return 1
			else:
				m=m+a[pos]
				pos+=1
				m=m-a[pos]
				b=a[pos+1:]

		return 0
t=int(input())
for asd in range (t):
	n,m=list(map(int,input().split()))
	a=[]
	for ssss in range (n):
		x=int(input())
		if(x<=m):
			a.append(x)
	a=sorted(a,reverse=True)
	sumi=sum(a)
	if (sumi<m):
		flag=0
	elif (sumi==m):
		flag=1
	else:
		flag=check(a,m)
	if flag==1:
		print("Yes")
	else:
		print("No") 

