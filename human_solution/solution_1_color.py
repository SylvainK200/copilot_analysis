for _ in range(eval(input())):
	r,g,b,n=0,0,0,eval(input())
	s=input()
	for i in s: 
		if i=='R': r+=1
		if i=='G': g+=1
		if i=='B': b+=1
	print(n-max(r,g,b))
