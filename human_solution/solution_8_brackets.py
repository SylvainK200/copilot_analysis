t = eval(input())
for _ in range(t):
    s = input()
    max_bal = 0
    bal = 0
    for c in s:
        if c == '(':
            bal += 1
        elif c == ')':
            bal -= 1
        max_bal = max(bal, max_bal)
    i = 0
    ans = ''
    while i < max_bal:
        ans += '('
        i += 1
    while i > 0:
        ans += ')'
        i -= 1
    print(ans)
