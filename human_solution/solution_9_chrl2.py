count = {'C': 0,'H': 0,'E': 0,'F': 0}
a = input()
length = len(a)
c = 0
ch = 0
che = 0
chef = 0
for i in range(0, length):
	if a[i] == 'C':
		c += 1
	elif c > 0 and a[i] == 'H':
		c -= 1
		ch += 1
	elif ch > 0 and a[i] == 'E':
		ch -= 1
		che += 1
	elif che > 0 and a[i] == 'F':
		che -= 1
		chef += 1
print(chef) 