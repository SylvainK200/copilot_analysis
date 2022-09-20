#!/usr/bin/python
for i in range(eval(input())):
	n=eval(input())
	string=input()
	if 'Y' in string:
		print("NOT INDIAN")
	elif 'I' in string:
		print("INDIAN")
	else:
		print("NOT SURE")

