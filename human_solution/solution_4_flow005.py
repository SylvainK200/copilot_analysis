def notes(n):	
	lst =[1,2,5,10,50,100]
	lst.reverse()
	count=0	
	for i in lst:
		while(n>=i):
			n=n-i
			count+=1
	return count
T=int(input())
for i in range(T):
	n=int(input())
	print(notes(n))