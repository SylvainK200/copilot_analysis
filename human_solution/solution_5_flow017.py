t=eval(input())
while t:
 t-=1
 a = list(map(int,input().split()))
 a.sort()
 print(a[1])