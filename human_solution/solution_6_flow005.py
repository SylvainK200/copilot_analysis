#!/usr/bin/python
currency=[100,50,10,5,2,1]
look_up={}
def get_count(N):
	if N==0:
		return 0
	if N in look_up:
		return look_up[N]
	else:
		for i in currency:
			if N/i>0:
				p=N/i
				N=N-p*i
				return p+get_count(N)
if __name__=='__main__':
	for i in range(eval(input())):
		print(get_count(eval(input())))

		
