varC = varH = varE = varF = 0
for x in input():
	if x == 'C':
		varC += 1
	elif x == 'H' and varC > varH:
		varH += 1
	elif x == 'E' and varH > varE:
		varE += 1
	elif x == 'F' and varE > varF:
		varF += 1
print(varF)
