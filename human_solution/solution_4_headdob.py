test = eval(input())
 
while test>0:
 
	test=test-1
 
	n=eval(input())
 
	string=input()
 
	if string.find('Y')!=-1 :
 
		print("NOT INDIAN")
 
	elif string.find('I')!=-1 :
 
		print("INDIAN")
 
	else:
 
		print("NOT SURE")

