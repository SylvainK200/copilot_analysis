# cook your code here
import math
n,k = [int(j) for j in input().split()]
a = [int(j) for j in input().split()]
 
dp = [0]*n
ans = [0]*n
current_index = 0
for i in range(n):
    if i <= k: 
        dp[i] = math.log(a[i])
        ans[i] = a[i]
    elif i - k - 1 == current_index:
        smallest, index = min((val, j) for (j,val) in enumerate(dp[current_index+1:i])) 
        dp[i] = math.log(a[i]) + smallest
        current_index += 1+index
        ans[i] = a[i] * ans[current_index] % 1000000007
    else:
        dp[i] = math.log(a[i]) + dp[current_index]
        ans[i] = a[i] * ans[current_index] % 1000000007
print(a[0]*ans[-1]%1000000007) 