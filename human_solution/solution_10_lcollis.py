for tc in range(eval(input())):
	boys,girls = list(map(int,input().split()))
	l = [[0 for girl in range(girls)] for boy in range(boys)]
	for boy in range(boys):
		inp = list(input())
		for girl in range(girls):
			if inp[girl] == '1':
				l[boy][girl] = 1
			
		
	collison = 0
	for girl in range(girls):
		count = 0
		for boy in range(boys):
			if l[boy][girl] == 1:
				count += 1
		collison += count * (count-1) / 2
	print(collison)
