t = int(input())

num = []
count=0
num = list(map(int,input().split()))
for i in range(0,len(num)):
    if num[i]%2==0:
        count+=1
if(count>(int(len(num)/2))):
    print("READY FOR BATTLE")
else:
    print("NOT READY")




