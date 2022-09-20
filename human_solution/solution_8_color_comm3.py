import math

def cal_dist(x1,y1,x2,y2):
	dis = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
	return dis

test = int(eval(input()))
while test:
	R = int(eval(input()))
	cx1,cy1=list(map(int, input().split()))
	cx2,cy2=list(map(int, input().split()))
	cx3,cy3=list(map(int, input().split()))
	d1 = cal_dist(cx1,cy1,cx2,cy2)
	d2 = cal_dist(cx1,cy1,cx3,cy3)
	d3 = cal_dist(cx3,cy3,cx2,cy2)
	if((d1<=R and d2<=R) or (d1<=R and d3<=R) or (d3<=R and d2<=R)):
		print("yes")
	else:
		print("no")
	test = test-1
	