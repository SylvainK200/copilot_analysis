for i in range(eval(input())):
	a,b,c = list(map(float, input().split()))
	if(a>50 and b<.7 and c>5600):
		print(10)
	elif(a>50 and b<.7):
		print(9)
	elif(b<.7 and c>5600):
		print(8)
	elif(a>50 and c>5600):
		print(7)
	elif(a>50 or b<.7 or c>5600):
		print(6)
	elif(a<=50 and b>=.7 and c<=5600):
		print(5)