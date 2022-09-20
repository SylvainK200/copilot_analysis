import heapq
from math import log
mod=10**9+7
n,k=list(map(int,input().split()))
li=list(map(int,input().split()))
dp=[0]*n
dp[0]=li[0]
heap=[]
heapq.heappush(heap,(log(dp[0]),0))
for i in range(1,k):
    dp[i]=(dp[0]*li[i])%mod
    heapq.heappush(heap,(log(dp[0])+log(li[i]),i))
for i in range(k,n):
    while heap[0][1]<i-k:
        heapq.heappop(heap)
    dp[i]=(dp[heap[0][1]]*li[i])%mod
    heapq.heappush(heap,(heap[0][0]+log(li[i]),i))
print(dp[n-1]%mod)
