#http://www.codechef.com/problems/ASTRGAME
def work():
    cas = int(input())
    for j in range(cas):
        initStr = input()
        n = int(input())
        dict = set()
        lth = len(initStr)
        dp = [[None for i in range(lth+1)] for j in range(lth+1)]
        for i in range(n):
            dict.add(input())
        res = solve(0, len(initStr)-1, initStr, dict, dp)
        if res == 0:
            print("Tracy")
        else:
            print("Teddy")


def solve(st, ed, initstr, dic, dp):
    if st > ed:
        return 0
    if dp[st][ed] is not None:
        return dp[st][ed]
    mex = set()
    for i in range(st, ed+1):
        for j in range(i, ed+1):
            # child positions
            if initstr[i:j+1] in dic:
                mex.add(solve(st, i-1, initstr, dic, dp) ^ solve(j+1, ed, initstr, dic, dp))
    i = 0
    while True:
        if i not in mex:
            break
        i += 1

    dp[st][ed] = i
    return i

work()

