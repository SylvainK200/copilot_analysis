t = int(input());
for i in range(t):
	s = '';
	n = int(input());
	if (360 % n == 0 ):
		s += 'y ';
	else:
		s += 'n ';
	
	if ( n <= 360 ):
		s += 'y ';
	else:
		s += 'n ';
	
	if ( n <= 26 ):
		s += 'y ';
	else:
		s += 'n ';
		
	print(s);