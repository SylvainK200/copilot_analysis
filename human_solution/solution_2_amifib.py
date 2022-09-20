l=[0,1,1,2,3,5,8,13,21,34]
for t in range(int(input())):
	n=int(input())
	if (n in l):
		print("YES")
	else:
		while (n>l[-1]):
			l.append(l[-1]+l[-2])
		if (n in l):
			print("YES")
		else:
			print("NO")