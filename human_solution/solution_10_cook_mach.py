#!/usr/bin/python
import sys
import math
t=int(input())
for i in range(0,t):
 sum=0
 x,y=list(map(int,sys.stdin.readline().split(" ")))
 while True :
  if (y%x==0):
   break
  else:
   x/=2
   sum+=1
 while(x!=y):
  x*=2
  sum+=1
 print(sum)
