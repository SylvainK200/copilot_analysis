inp = int(input(""))
list = []
for c in range(inp):
    b = int(input(""))
    hun = b/100
    fif = (b - hun*100)/50
    ten = (b - hun*100 - fif*50)/10
    fiv = (b - hun*100 - fif*50 - ten*10)/5
    two = (b - hun*100 - fif*50 - ten*10 - fiv*5)/2
    one = (b - hun*100 - fif*50 - ten*10 - fiv*5 - two*2)
    no = hun + fif + fiv + ten + two + one
    list.append(no)

for c in range(inp):
    print((list[c]))