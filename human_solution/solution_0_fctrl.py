t = int(input())
while t!=0:
 a = int(input())
 l1 = []
 i = 1
 c = 0
 while True:
  if(a>=5**i):
   z = a/(5**i)
   l1.append(z)
   i+=1
  else:
   break
   
 for i in range(0,len(l1)):
  c = c+l1[i]

 print(c)  
 t-=1