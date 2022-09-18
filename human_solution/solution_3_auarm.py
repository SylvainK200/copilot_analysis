list=[]
for i in range(eval(input())):
	n,m=list(map(int,input().split()))
	# list=map(int,raw_input().split());
	list=input()
	list=list(map(int,list.split()))
	ma=(max(list))
	mi=(min(list))
	for j in range(n):
		if (ma-j)>(j-mi):
			print(ma-j, end=' ')	
		else:
			print(j-mi, end=' ')
	print('')
	
