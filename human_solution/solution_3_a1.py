from sys import stdin
from itertools import combinations 

T=int(stdin.readline())
s=set()
for t in range(T):

	notes,demand=list(map(int,stdin.readline().split()))
	i=0
	flag=False;
	wallet=list()
	filter_wallet=list()
	
	for n in range(notes):
		i=int(stdin.readline())
		wallet.append(i)

	wallet.sort(reverse=True)
	filter_wallet=[x for x in wallet if x <=demand]
	
	if demand in filter_wallet:
		flag=True
		
	else :
		
		for j in range(len(filter_wallet)+1):
			if(flag== False):
				for combination in combinations(filter_wallet,j+2):					
					if sum(combination)==demand:
						flag = True
						break
			else:
				break
	
	if flag==True:
		print("Yes")
	else:
		print("No")

	
		
		
	


