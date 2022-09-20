t=int(input())
den=33102
for asd in range (t):
	n=int(input())
	ans="3"
	if (n>0):
		ans+='.'
		num=103993
		for dsf in range (n):
			num=(num%den)
			num*=10
			ans+=str(num/den)
	print(ans)
		