t = eval(input())
while(t>0):
	t-=1
	r = eval(input())
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))
	c=list(map(int,input().split()))
	count=0
	if( (a[0]-b[0])**2 +(a[1]-b[1])**2 <=r**2 ):
		count+=1
	if( (b[0]-c[0])**2 +(c[1]-b[1])**2 <=r**2):
		count+=1
	if( (c[0]-a[0])**2 +(c[1]-a[1])**2 <=r**2):
		count+=1
	if(count>=2):
		print("yes")
	else:
		print("no")