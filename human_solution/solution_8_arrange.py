T = int(input(''))

def Decimal_To_Binary(x, n):
    ans = ''
    if x == 0 or x == 1:
        ans += str(x)
    else:
        ans += Decimal_To_Binary(x/2, n-1) + str(x % 2)
    if len(ans) < n:
        return '0'*(n-len(ans)) + ans
    return ans

def Find_Index(B, n):
    ans = 0
    for i in range(n):
        ans += (2**i)*int(B[i])
    return ans

def Arrange_App(L, S, k):
    for i in range(1, 2**k - 1):
        if L[i] == None:
            bi = Decimal_To_Binary(i, k)
            j = Find_Index(bi, k)
            L[i] = S[j]
            L[j] = S[i]
    return L

for i in range(T):
    k, S = input('').split(' ')
    k = int(k)
    L = []
    for j in range(2**k):
        L.append(None)
    L[0] = S[0]
    L[-1] = S[-1]
    L = Arrange_App(L, S, k)
    print(''.join(L))
