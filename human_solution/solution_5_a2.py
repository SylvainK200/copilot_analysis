def check():
	a=[]
	k=int(input())
	a[0:]=list(map(int,input().split()))
	s=0.5
	for i in range(len(a)):
		s=s*2-a[i]
	if s == 0:
		return 1
	else:
		return 0

def main():
	m=0	
	j=int(input())
	while m<j:
		if(check()):
			print("Yes")
		else:
			print("No")
	 	m=m+1
	return 
if __name__=="__main__":
	main()