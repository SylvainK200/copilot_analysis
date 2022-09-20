T = int(input())
 
sol = [int(x) for x in input().rstrip().split(" ")]
 
even = 0
odd = 0
for x in sol:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1
if even > odd:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
 
