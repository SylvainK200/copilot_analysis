# your code goes here
T = eval(input());
for x in range(0,T):
	NM = input();
	NM = NM.split();
	N = int(NM[0]);
	arr = [];
	for y in range(0,N):
		arr.append(y);
	M = input();
	values = M.split();
	for y in range(0,len(values)):
		values[y] = int(values[y]);
	high = max(values);
	low = min(values);
	max1 = [];
	min1 = [];
	for y in range(0,N):
		max1.append(abs(arr[y]-high));
		min1.append(abs(arr[y]-low));
	max_arr = [];
	for y in range(0,N):
		max_arr.append(str(max(max1[y],min1[y])));
	print(" ".join(max_arr));