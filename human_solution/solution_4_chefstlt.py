import sys
test_cases = int(sys.stdin.readline())
while(test_cases > 0):
    test_cases -= 1
    str1 = sys.stdin.readline()
    str2 = sys.stdin.readline()
    min_diff = 0
    max_diff = 0
    q_str = 0
    len = str1.__len__()
    for i in range(0, len):
        if((str1[i] != str2[i]) or (str1[i] == '?') or (str2[i] == '?')):
            if(str1[i] == '?' or str2[i] == '?'): q_str += 1
            max_diff += 1
    min_diff = max_diff - q_str
    print(min_diff, max_diff)