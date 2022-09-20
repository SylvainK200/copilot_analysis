n=int(input())
weapons=[]
if(n<1 or n>100):
    exit()
weapons=list(map(int,input().split(" ")))
if(len(weapons)!=n):
    exit()
odd_count=0
even_count=0
for i in range(0,n):
    test=weapons[i]
    x=test%2
    if(x==0):
        even_count+=1
    else:
        odd_count+=1
if(even_count>odd_count):
    print("READY FOR BATTLE")
else:
    print("NOT READY")
