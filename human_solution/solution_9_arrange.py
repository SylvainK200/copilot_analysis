"""
pensando aqui

110 -> 011
6 -> 3
0101 -> 1010
5 -> 10
100000011 -> 110000001
259 -> 385

eh soh inverter

"""

def bin_to_n(bin):
	sum = 0
	for i in range(len(bin)):
		sum += bin[i] * 2**i
	return sum

def ad_hoc(k,acc,sA,sB):
	if len(acc)==k:
		bin = acc
		binrev = list(reversed(bin))	#it's crucial that it not be in-place
		a = bin_to_n(bin)
		b = bin_to_n(binrev)
		sB[b] = sA[a]
	else:
		ad_hoc(k, acc+[0], sA, sB)
		ad_hoc(k, acc+[1], sA, sB)




T = int(input())

while T>0:
	T-=1
	k, string = input().split()
	k = int(k)
	N = 2**k	#max(k) = 16, entao max(N)=65536
	sB = list(range(N))

	ad_hoc(k, [], string, sB)
	print(("".join(sB)))