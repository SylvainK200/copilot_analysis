import string;
x = input();
flag = 0;
strin ='';
#strinlist = [];
current_max = 0;
for i in x:
	if len(strin) > 0 and strin[0] == '0':
		strin = strin[1:];    
	if i in '1234567890':
		strin += i;
	elif i in string.ascii_uppercase and flag == 0:
		strin += i;
		flag = 1;
	elif i in string.ascii_uppercase and flag == 1:
		strin += i;
		for j in strin:
			if j in string.ascii_uppercase:
				index = strin.index(j);
				strin = strin[index + 1:];
				break;
	if len(strin) > current_max:
		strinlist = [];		
		strinlist.append(strin);
		current_max = len(strin);	
	elif len(strin)	== current_max:
		strinlist.append(strin);
#print strinlist;

max1 = 0;
for m in strinlist:
	for j in m:
		if j in string.ascii_uppercase:
			m = m[:m.index(j)] +'9'+ m[m.index(j) + 1:]
			break;
	if int(m)>max1:
#		print int(m);
		max1 = int(m);
print(max1);
