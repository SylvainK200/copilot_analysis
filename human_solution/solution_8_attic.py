cases=int(input())
while cases:
	a=input();
	i=1
	max=0
	m=0
	length=len(a)
	while i<length:
		if a[i] is '.':
			k=0	
			while a[i]=='.':
					i+=1
					k+=1
			count=k
			if count>max:
				max=count
				m+=1
		
		else:
			i+=1
	print(m)
	cases-=1		
			
	
		
	
	
