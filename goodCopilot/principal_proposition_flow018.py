"""
Write a program to find the factorial value of any number entered by the user.


Input
The first line contains an integer †T‡, total number of testcases. Then follow †T‡ lines, each line contains an integer †N‡.


Output
Display the factorial of the given number †N‡ .

Constraints

1 †≤‡ †T‡ †≤‡ 1000
0 †≤‡ †N‡ †≤‡ 20


Example

†Input‡
3 
3 
4
5

†Output‡

6
24
120
"""
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

t = int(input())
for i in range(t):
    n = int(input())
    print(factorial(n))