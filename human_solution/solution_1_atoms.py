# your code goes here
for _ in range(eval(input())):
	a=input()
	n=eval(input())
	l=[[]for i in range(26)]
	sizes =[0]*26
	for i in range(len(a)):
		ind=ord(a[i])-97
		l[ind].append(i)
		sizes[ind]+=1
	#print l
	ans=""
	ln=len(a)
	current=-1
	for i in range(n):
		for j in range(26):
			while(sizes[j]>0 and l[j][0]<=current ):
				temp=l[j][0]
				l[j].remove(temp)
				sizes[j]-=1
			if(sizes[j]!=0):
				
				if(l[j][0]+(n-i)<=ln):
					ans+=chr(j+97)
					sizes[j]-=1
					temp=l[j][0]
					current=temp
					l[j].remove(temp)
					break
	print(ans)