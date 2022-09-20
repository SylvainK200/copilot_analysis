T = eval(input())
for test in range(T):
	A, B, C = list(map(int, input().split()))
	if (A==180 or B==180 or C==180):
		print("NO")
	elif A+B+C == 180 and (A>0 and B>0 and C>0 and A<180 and B<180 and C<180):
		print("YES")
	else:
		print("NO")
