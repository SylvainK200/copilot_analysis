import sys

for __ in range(eval(input())) :
    n , m = list(map(int,sys.stdin.readline().split()))
    print("%.6f"%(n+m-1))