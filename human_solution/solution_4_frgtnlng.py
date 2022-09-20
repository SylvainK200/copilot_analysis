# your code goes here
t = int(input())
for sc in range(t):
	n, k = list(map(int, input().split()))
	lang = input().split()
	d={}
	for i in lang:
		d[i] = 0
	for phr in range(k):
		phrase = input().split()
		for i in phrase[1:]:
			if i in lang:
				d[i] += 1
	ans = ""
	for i in lang:
		if d[i] > 0:
			ans+="YES "
		else:
			ans+="NO "
	print(ans.strip())