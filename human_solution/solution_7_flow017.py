#!/usr/bin/env/ python
#FLOW017
#https://www.codechef.com/problems/FLOW017
t=eval(input())
while t!=0:
	t-=1
	print((sorted(map(int,input().split())))[1])
