def ans(l,k):
	n = len(l)
	if (n%(k+1) == 0):
		k = n/(k+1)
	else:
		k = (n/(k+1)) + 1
	return (l[k-1])

n = int(eval(input()))
l = list(map(int,input().split()))
l.sort()
i = 0
s = 0
while (i < len(l)):
	s += l[i]
	l[i] = s
	i += 1
q = int(eval(input()))
while (q != 0):
	k = int(eval(input()))
	q -= 1
	print((ans(l,k)))
