def main():
	test = int(input())
	for t in range(test):
		if check():
			print("Yes")
		else:
			print("No")

def check():
	levels = int(input())
	maxleaf = 0.5
	leaf = list(map(int,input().split()))
	for i in range(levels):
		maxleaf = 2*maxleaf-leaf[i]
	return maxleaf==0
		
if __name__=="__main__":
	main()