a = eval(input())
l1 = []
b = input().split()
for c in b:
    l1.append(int(c))
l2 = []
l3 = []
for d in l1:
    if d % 2== 0:
        l2.append(d)
    else:
        l3.append(d)
 
if len(l2) > len(l3):
    print("READY FOR BATTLE")
else:
    print("NOT READY")