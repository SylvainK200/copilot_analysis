import time, datetime

def print_day(index):
	if(index==0):
		print("monday")
	elif(index==1):
		print("tuesday")
	elif(index==2):
		print("wednesday")
	elif(index==3):
		print("thursday")
	elif(index==4):
		print("friday")
	elif(index==5):
		print("saturday")
	elif(index==6):
		print("sunday")
	else:
		print("error")

T=eval(input())
while(T!=0):
	n=eval(input())
	dt=datetime.datetime(year=n,month=1,day=1)
	print_day(dt.weekday())
	T-=1
