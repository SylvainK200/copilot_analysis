N,M=[int(x) for x in input().split()]
sumarr=[0]*N
tenarr=[0]*10
arr=input().strip()
j=0
for i in arr:
    tenarr[int(i)]+=1
    for a in range(0,10):
        sumarr[j]+=(tenarr[a]*abs(int(i)-a))
    j+=1
while M:
    M-=1
    B=eval(input())
    print(sumarr[B-1])