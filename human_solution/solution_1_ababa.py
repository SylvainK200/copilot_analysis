for t in range(int(input())):
	s = input()
	n = len(s)
	a = s.count('A')
	b = n-a 
	if (a==2):
		print("A")
	elif (b==2):
		print("B")
	elif (n<4):
		print(-1)
	else:
		if (s[0]=="A"):
			s = "B"+s
		else:
			s = "A"+s
		if (s[-1]=="A"):
			s = s+"B"
		else:
			s = s+"A"
		pos1 = s.find("ABBA")
		pos2 = s.find("BAAB")
		if (pos1 == -1 and pos2 == -1):
			print(-1)
		else:
			if (pos1 == -1):
				pos = pos2
			elif (pos2 == -1):
				pos = pos1
			else:
				pos = min(pos1, pos2)
			print(s[1:pos+1]+s[pos+2:-1])
			
		