#!/usr/bin/python
from sys import stdin
def main():
	with stdin as f:
		t = f.readline();
		s= 0.5
		for i in range(int(t)):
			n = int(f.readline());
			l = list(map(int,f.readline().split(' ')));
			for j in range(n):
				s = 2*s-l[j]
			if s==0:
				print('Yes')
			else:
				print('No')
			s = 0.5
if __name__ == '__main__': main()