# @author Kilari Teja
# LCOLLIS


for Indx in range(0, int(input())):
	Collisions = 0
	Dims = [int(Dim) for Dim in (input()).split(" ")]

	Cols = [[] for CIndx in range(0, Dims[1])]
	for RIndx in range(0, Dims[0]):
		Row = input()
		for Chr in range(0, Dims[1]):
			Cols[Chr].append(Row[Chr])

	for Col in Cols:
		Occour = Col.count('1')
		for S in range(1, Occour):
			Collisions = Collisions + S

	print(Collisions)