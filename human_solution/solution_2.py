# create atoms from the input
tc=int(input())

for i in range(tc):
	n_m = (input())
	n = int(n_m.split()[0])
	m = int(n_m.split()[1])
	#generate list of atoms
	atoms=[]
	for j in range(n):
		atoms.append(j)
	atomlist = ['']*n

	for k in range(m):
		s=[]
		s.extend(input().split()[1:])	
		for w in range(n):
			if str(w) in s:
				atomlist[w]+="1"
			else:
				atomlist[w]+="0"

	print(len(set(atomlist)))


		
