n = eval(input())
a = [0]*100
a = input().split(" ")
c1 =0 
c2 =0
c = 0
for i in range(0, n):
	c = int(a[i]) 
	if(c%2==0):
		c1 += 1
	else :
		c2 += 1 
if(c1>c2):
	print("READY FOR BATTLE")
else : 
	print("NOT READY")