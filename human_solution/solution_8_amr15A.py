cnte = 0
cnto = 0
n = int(input())
a = list(map(int,input().split()))
for x in a:
    if x%2: cnto+=1
    else: cnte+=1
if cnte > cnto: print("READY FOR BATTLE")
else: print("NOT READY")
