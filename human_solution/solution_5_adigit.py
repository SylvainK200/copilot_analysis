n,m=input().split()
n=int(n)
x=input()
summ={}
summ[0]=0
for i in range(1,n):
	summ[i]=0
	j=i-1
	while 1:
		if j==-1: break
		elif x[i]==x[j]:
			summ[i]+=summ[j]
			break
		else:
			summ[i]+=abs(int(x[i])-int(x[j]))
			j+=-1
for i in range(0,int(m)):
	print(summ[eval(input())-1])