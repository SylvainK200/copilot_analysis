import math
def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

import math
n = int(input())
rs = []
while n != 0:
    max_d = int(input())
    p1 = list(map(int,input().split()))
    p2 = list(map(int,input().split()))
    p3 = list(map(int,input().split()))
    ds = []
    ds.append(distance(p1[0], p1[1], p2[0], p2[1]))
    ds.append(distance(p1[0], p1[1], p3[0], p3[1]))
    ds.append(distance(p2[0], p2[1], p3[0], p3[1]))
    ds = sorted(ds)
    if ds[0] <= max_d and ds[1] <= max_d:
        rs.append("yes")
    else:
        rs.append("no")
    n -= 1

for i in rs:
    print(i)