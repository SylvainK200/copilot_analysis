import numpy as np
T=int(input())
for i in range(T,0,-1):
	N,M=[int(x) for x in input().split()]
	A=np.zeros((N,M))
	ans=np.zeros(M)
	for nl in range(0,N,1):
		temp=input()
		cnt=0
		for tc in list(temp):
			A[nl][cnt]=int(tc)
			cnt+=1
	sumcnt=0		
	for ml in range(0,M,1):
	    for nlo in range(0,N-1,1):
	        for nll in range(nlo+1,N,1):
	           sumcnt+= A[nlo,ml] and A[nll,ml]
	    ans[ml]=sumcnt
	    sumcnt=0
	final=ans.sum(dtype=np.int32)
	print(final)