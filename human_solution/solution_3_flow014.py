# @author Kilari Teja
# FLOW014

for _ in range(int(input().strip())):
	[Hardness, Carbon, Tensile] = list(map(float, input().strip().split()))

	HardnessFlag = False
	CarbonFlag   = False
	TensileFlag  = False

	if Hardness > 50:
		HardnessFlag = True
	if Carbon < 0.7:
		CarbonFlag = True
	if Tensile > 5600:
		TensileFlag = True

	Grade = 0
	# Geade The Steel Here !
	if HardnessFlag and CarbonFlag and TensileFlag:
		Grade = 10
	elif HardnessFlag and CarbonFlag:
		Grade = 9
	elif CarbonFlag and TensileFlag:
		Grade = 8
	elif HardnessFlag and TensileFlag:
		Grade = 7
	elif HardnessFlag or CarbonFlag or TensileFlag:
		Grade = 6
	else:
		Grade = 5

	print(Grade)