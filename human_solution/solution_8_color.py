#Practice problem: Coloring the rooms
num_of_tests=int(input())
if num_of_tests>10:
	exit(1)
input_nor=[]
input_color=[]
for i in range(0,num_of_tests):
	nor=input()
	if int(nor)>100000:
		exit(1)
	color_str=input()
	for k in range(0,len(color_str)):
		if color_str[k]!='R' and color_str[k]!='G' and color_str[k]!='B':
			exit(1)
	input_nor.append(nor)
	input_color.append(color_str)

l=len(input_color)
color_dict=dict()
color_dict['R']=0
color_dict['G']=0
color_dict['B']=0
for i in range(0,l):
	color_dict=dict()
	color_dict['R']=0
	color_dict['G']=0
	color_dict['B']=0
	result=0
	nor=input_nor[i]
	color_str=input_color[i]
	for j in color_str:
		if j=='R':
			color_dict['R']+=1
		elif j=='G':
			color_dict['G']+=1
		elif j=='B':
			color_dict['B']+=1
	if color_dict['R']==0 and color_dict['G']==0:
		result=0
	elif color_dict['R']==0 and color_dict['B']==0:
		result=0
	elif color_dict['G']==0 and color_dict['B']==0:
		result=0
	else:
		sum1=color_dict['R']+color_dict['G']+color_dict['B']
		m=max(color_dict.values())
		result=sum1-m
	print(result)


