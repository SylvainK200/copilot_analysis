# Chef and string- CHRL2 

Str= input()  # gets the input string

c = ch = che = chef = 0
time = 0
for i in Str:
	if (i == 'c' or i == 'C'):
		c += 1
	elif (i == 'h' or i == 'H') and (c > 0):	
		c -= 1
		ch += 1
	elif (i == 'e' or i == 'E') and (ch > 0):	
		ch -= 1
		che += 1
	elif (i == 'f' or i == 'F') and (che > 0):	
		che -= 1
		chef += 1
		
print(chef)  # number of times chef was formulated