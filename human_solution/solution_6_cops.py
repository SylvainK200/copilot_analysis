""" Cops and the Thief Devu """

t = int(input())
for i in range(t):
    # Import parameters
    M, x, y = list(map(int, input().split(" ")))
    lst = list(map(int, input().split(" ")))
    
    # Look for the period (of danger houses)
    xy_lst = [ x * y for j in range(M)]
    lst_sub = [a - b if (a - b) > 0 else 1 for a, b in zip(lst, xy_lst)]
    lst_add = [a + b if (a + b) < 101 else 100 for a, b in zip(lst, xy_lst)]
    
    # Calculate the # of safe houses
    ones = [1 for j in range(100)]
    for idx in range(M):
        ones[lst_sub[idx]-1:lst_add[idx]-1+1] = [0 for j in range(lst_add[idx] - lst_sub[idx] + 1)]

    print(sum(ones))