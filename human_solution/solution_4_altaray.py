from sys import stdin
from math import copysign
def printBS(li):
 print(" ".join([str(x) for x in li]))
def listInput():
 return list(map(int,stdin.readline().split()))
cases=eval(input())
for case in range(cases):
 n=eval(input())
 li=listInput()
 dp=[0]*n
 dp[-1]=1
 for i in range(n-2,-1,-1):
  if li[i+1] and li[i] and copysign(1,li[i])!=copysign(1,li[i+1]):
   dp[i]=dp[i+1]+1
  else: dp[i]=1
 printBS(dp)