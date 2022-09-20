import sys

n = eval(input())
lists = list(map(int,sys.stdin.readline().split()))
lists.sort()
pref = [0]*(n+1)
pref[0] = lists[0]
for i in range(1,n) :
    pref[i] = pref[i-1]
    pref[i] += lists[i]
for __ in range(eval(input())) :
    k = eval(input())
    print(pref[n/(k+1)] if n%(k+1) else pref[(n/(k+1)-1)])
