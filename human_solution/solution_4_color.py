t=int(input())
for i in range(t) :
	n= int(input())
	s = str(input())
	i=0
	r=0
	g=0
	b=0
	while i < len(s):
		if s[i]=='R':
			r+=1
		elif s[i]=='G':
			g+=1
		else:
			b+=1
		
		i += 1
	m = max(r,b,g)
	print(n-m)
	r=0
	b=0
	g=0
