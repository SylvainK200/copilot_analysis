buf=input()

dp=[0]*1002
dpc=[0]*1002

if buf[0].isdigit():
	dp[0]=0
	dpc[0]=0
else:
	dp[0]=-1
	dpc[0]=0

for i in range(1, len(buf)):
	if buf[i].isdigit():
		dp[i] = dp[i-1] if dp[i-1]!=-1 else i
		dpc[i] = dpc[i-1] if dpc[i-1]!=-1 else i
	else:
		dp[i] = -1
		dpc[i] = dp[i-1] if dp[i-1]!=-1 else i

mx = -1
for i in range(0, len(buf)):
	if dpc[i]!=-1:
		#print buf[dpc[i]: i+1]
		mys=''
		for x in range(dpc[i], i+1):
			mys += buf[x] if buf[x].isdigit() else '9'
		#print mys
		if int(mys)>mx:
			mx=int(mys)
print(mx)