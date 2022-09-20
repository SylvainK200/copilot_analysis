def main():
	T=int(input())
	for t in range(T):
		z=[]
		s=str("")
		X= list(input())
		Y= list(input())
		for n in range(len(X)):
			if(X[n]==Y[n]=="W"):
				z.append("B")
			elif(X[n]==Y[n]=="B"):
				z.append("W")
			else:
				z.append("B")
		z=s.join(z)
		print(z)	
main()			

