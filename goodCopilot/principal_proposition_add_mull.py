"""You are given a one dimensional integer array †A‡ of length †N‡. You need to maintain the array under †Q‡ queries of the following four types. Assume 1-based indexing and M = 10^9 + 7.
†Query 1‡ : 1 x y v  This implies adding v to array †A‡ to all the indices from x to y, i.e., 
for (i = x; i <= y; i++)	
	†A‡i += v;
	†A‡i %= M; 

 
†Query 2‡ : 2 x y v  This implies multiplying the scalar v with the array †A‡ for all the indices from x to y, i.e., 
for (i = x; i <= y; i++)	
        †A‡i *= v
        †A‡i %= M

 
†Query 3‡ : 3 x y v  This implies initializing the array †A‡ at all the indices from x to y with the value v, i.e., 
for (i = x; i <= y; i++)	
	†A‡i = v 

 
†Query 4‡ : 4 x y This is a report query which needs to find the sum of the values in †A‡ from x to y, i.e., 
sum = 0;
for (i = x; i <= y; i++)
	sum += †A‡i
	sum %= M
Output sum.

 
†Note:‡ a%b represents the remainder of a when divided by b.

Input

First line contains two space separated integers †N‡, †Q‡.
Next line contains †N‡ space separated integers denoting the array †A‡.
Next †Q‡ lines contain queries which can be of any of the above four types.


Output

For each query of type 4, output a single integer corresponding to the answer in a single line.


Constraints

1 ≤ †N‡ ≤ 10^5
1 ≤ †Q‡ ≤ 10^5
1 ≤ Initial value of †A‡i ≤ 10^9
1 ≤ †v‡ ≤ 10^9


Example
Input:
4 4
1 2 3 4
4 1 4 0
1 1 3 10
2 2 4 2
4 1 4 0 

Output:
10
69



Explanation
Initial †A‡ : [1, 2, 3, 4] Result of first query : 1 + 2 + 3 + 4 = 10 †A‡ after second query: [ 11, 12, 13, 4] †A‡ after third query : [ 11, 24, 26, 8] Result of fourth query : 11 + 24 + 26 + 8 = 69"""
n, q = map(int, input().split())
a = list(map(int, input().split()))
for _ in range(q):
    qtype, x, y, v = map(int, input().split())
    if qtype == 1:
        for i in range(x-1, y):
            a[i] += v
            a[i] %= 1000000007
    elif qtype == 2:
        for i in range(x-1, y):
            a[i] *= v
            a[i] %= 1000000007
    elif qtype == 3:
        for i in range(x-1, y):
            a[i] = v
    else:
        sum = 0
        for i in range(x-1, y):
            sum += a[i]
            sum %= 1000000007
        print(sum)