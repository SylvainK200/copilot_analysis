# Hello World program in Python
def F(S):
	balance = 0
	max_balance = 0
	for item in S:
		if item == '(':
		    balance = balance + 1
		if item == ')' :
		    balance = balance - 1
		max_balance = max( max_balance, balance )
	return max_balance


T = input()
t = int(T)
while t>0:
    t=t-1
    A=input()
    list1 = [item for item in A]  
    n = F(list1)
    result = '('*n
    result = result + ')'*n
    print(result)