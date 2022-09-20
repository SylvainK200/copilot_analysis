from sys import stdin
test = int(stdin.readline())
n='3'
for i in range(test):
	d=int(stdin.readline())
	s=''
	r=103993
	for j in range(d):
		r=(r%33102)*10
		re=r/33102
		s=s+str(re)
	if d==0:
		print(n)
	else:
		print(n+'.'+s)