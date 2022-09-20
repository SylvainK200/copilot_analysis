import math
def sq(n):
	s= math.sqrt(n)	
	return int(s)
T=int(input())
for i in range(T):
		n=int(input())
		print(sq(n))