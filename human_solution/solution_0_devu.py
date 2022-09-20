tc = eval(input())
for i in range(tc):
   buk,k = input().split()
   buk,k = int(buk),int(k)
   gr = list(map(int,input().split()))
   m=0
   for j in range(buk):
      if gr[j]>k:
        mod = gr[j]%k
        m+=min(mod,k-mod)
      else:
         m+=k-gr[j]
   print(m)