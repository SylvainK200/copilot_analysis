n = int(input())
l = list(map(int, input().split()))
oc, ec = 0, 0
for i in l:
	if i%2==0:
		ec+=1
	else:
		oc+=1
if ec > oc:
	print("READY FOR BATTLE")
else:
	print("NOT READY")
