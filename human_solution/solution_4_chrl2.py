s=input()
c=ch=che=chef=0
for i in s:
	if i=="C":
		c+=1
	elif i=="H" and c>=1:
		ch+=1
		c-=1
	elif i=="E" and ch>=1:
		che+=1
		ch-=1
	elif i=="F" and che>=1:
		chef+=1
		che-=1
print(chef) 