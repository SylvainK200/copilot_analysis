import math

def isperfectsquare(n):
	root  = isqrt(n)
	
	if(int(root*root) == n):
		return True
	else:
		return False
def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def checkfib(n):
	if(isperfectsquare(5*n*n+4) or isperfectsquare(5*n*n-4)):
		return True
	else:
		return False

def main():
	t=input()

	for i in range (0,int(t)):
		n = input()
		n=int(n)
		if(checkfib(n) == True):
			print("YES")
		else :
			print("NO")


if __name__ == "__main__":
    main()
