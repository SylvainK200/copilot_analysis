for _ in range(eval(input())):
	s=input()
	c=days=i=m=0
	while i<len(s):
		c=0
		while s[i]=='.':
			c+=1
			i+=1
		i+=1
		days+=1 if c>m else 0
		m=max(c,m)	
	print(days)	