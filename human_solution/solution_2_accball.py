t = eval(input())
o=[]
for i in range(t):
	l1 = input()
	l2 = input()
	l3 = []

	for j in range(len(l1)):
		if l1[j] != l2[j] or l1[j]=='W':
			l3.append('B')
		else:
			l3.append('W')
	o.append(''.join(l3))

for e in o:
	print(e)

