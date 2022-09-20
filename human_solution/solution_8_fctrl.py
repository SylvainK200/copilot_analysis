def trailing_zeros_in_fctrl(x):
    z = 0
    r = x
    while r >= 5:
        z += int(r/5)
        r = int(r/5)
    return z


T = int(input())
for t in range(T):
    x = int(input())
    print(trailing_zeros_in_fctrl(x))