'''input
2
4 3
111
100
110
000
2 2
10
01
'''

#~~~~~~~~~~~~~~~~~~~~dwij28 == Abhinav Jha~~~~~~~~~~~~~~~~~~~~#

from sys import stdin, stdout
from math import sqrt, floor, ceil, log
from collections import defaultdict, Counter

def read(): return stdin.readline().strip()
def write(x): stdout.write(str(x))
def endl(): write("\n")

for T in range(int(read())):
	n, m = list(map(int, read().split()))
	data, ans = [], 0
	for N in range(n): data.append(read())
	for i in range(m):
		c = 0
		for j in range(n):
			if data[j][i] == '1': c += 1
		ans += c*(c-1)/2
	write(ans)
	endl()