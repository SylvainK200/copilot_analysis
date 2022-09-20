
import sys

def main():
	str = sys.stdin.readline().strip()
	
	alph = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	err = "9"
	maxage = 0
	ind = 0
	strLen = len(str)
	
	while ind < strLen:
		tmpstr = ""
		nochar = 1
		for i in range(ind, strLen):
			if str[i] not in alph:
				tmpstr += str[i]
				if nochar:
					ind += 1
			elif nochar:
				nochar = 0
				tmpstr += err
			else:
				break
		ind += 1
		
		tmpage = int(tmpstr)
		if tmpage > maxage:
			maxage = tmpage
	
	print(maxage)
	
	return 0

if __name__ == '__main__':
	main()
