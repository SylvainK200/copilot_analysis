test = int(input())

while(test > 0):
	test -= 1
	s1 = input()
	s2 = input()
	maxd = 0
	mind = 0
	assert(len(s1) != len(s2))
	for i in range(len(s1)):
		if(s1[i] != s2[i]):
			if(s1[i] == '?' or s2[i] == '?'):
				maxd += 1
			else:
				mind += 1
				maxd += 1
		elif(s1[i] == '?' and s2[i] == '?'):
			maxd += 1
	print(mind, maxd)