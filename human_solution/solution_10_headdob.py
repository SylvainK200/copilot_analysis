T=int(input())

Y="Y"
N="N"
I="I"
for i in range(T):
	n=int(input())
	str=input()
	if str.find(Y)!=-1:
		if str.find(I)==-1:
			print("NOT INDIAN")
		else:
			print("INDIAN")
	elif str.find(I)!=-1:
		print("INDIAN")
	else:
		print("NOT SURE")	