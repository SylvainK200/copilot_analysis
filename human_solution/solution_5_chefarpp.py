def product(li):
	p = 1
	for i in li:
		p *= i
	return p
test = eval(input())
for i in range(test):
	n = eval(input())
	arr = list(map(int, input().split()))
	count = 0
	for i in range(n+1):
		for j in range(i,n+1):
			if(sum(arr[i:j]) == product(arr[i:j])):
				count += 1
			
	print(count)