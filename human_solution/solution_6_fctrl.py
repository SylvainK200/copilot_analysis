# your code goes here
import math
test = int(input())
for _ in range(test):
	n = int(input())
	i = 1
	two_count = 0;
	five_count=int(0)
	while n/5**i>0:
		five_count+=int(math.floor(n/5**i))
		i+=1
	print(five_count)
		
	
