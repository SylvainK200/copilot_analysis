def f(t):
    """
    >>> f(0)
    3
    >>> f(6)
    3.141592
    >>> f(20)
    3.14159265301190260407
    """
    if t == 0:
        print(3)
    else:
        b = 103993 % 33102
        a = "3."
        for j in range(t):
            b *= 10
            if b < 33102:
                a += "0"
            else:
                a += str(b / 33102)
                b %= 33102
        print(a)


for i in range(int(input())):
    t = int(input())
    f(t)


