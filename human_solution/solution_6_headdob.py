t = int(input())
for i in range (0,t):
	n = int(input())
	m = input()
	m1 = m[0:n+1]
	if m1.find('Y')!= -1 :
		print("NOT INDIAN")
	elif m1.find('I')!=-1:
		print("INDIAN")
	else:
		print("NOT SURE")		