#!/usr/bin/python
a,b=input().split()
a=int(a)
b=float(b)
if(a%5==0 and a<b-0.5):
 b=b-a-0.5;
print("%0.2f" %b)