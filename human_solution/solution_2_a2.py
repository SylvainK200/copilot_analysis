import sys
for x in range(int(sys.stdin.readline())):
    numlevels = int(sys.stdin.readline())
    arr = sys.stdin.readline().split()
    arr = [int(y) for y in arr]
    numleaves = 0.5
    for z in range(numlevels):
        numleaves = numleaves*2 - arr[z]
    if (numleaves == 0):
        print("Yes")
    else:
        print("No")



