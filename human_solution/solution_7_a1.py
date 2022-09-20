import sys

def subset_sum(seq, num_notes, target):
    if target == 0: 
        return True
    if num_notes == 0 and target > 0:
        return False
    if seq[num_notes-1] > target:
	    return subset_sum(seq,num_notes-1,target)
    if subset_sum(seq,num_notes-1,target) or subset_sum(seq,num_notes-1,target-seq[num_notes-1]) == True:
	    return True


j=int(sys.stdin.readline().rstrip())
for i in range(j):
	num_notes,change_req=[int(l) for l in sys.stdin.readline().rstrip().split()]
	#a=[int(raw_input()) for x in xrange(num_notes)]
	notes = num_notes
	seq = []
	while notes!= 0:
		notes -= 1
		seq.append(int(sys.stdin.readline().rstrip()))
	
	if subset_sum(seq,num_notes,change_req):
		print("Yes")
	else:
		print("No")

 