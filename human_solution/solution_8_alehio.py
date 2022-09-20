from sys import stdin
import re
from string import uppercase as UC

S=stdin.readline().strip()
lenS = len(S)
maxAge = 0
for i in range(lenS):
    newS = S[:i] + "9" + S[i+1:] if S[i] in UC else S
    age = max(list(map(int,re.sub('[A-Z]+',''' ''',newS).split())))
    if age>maxAge: maxAge=age
print(maxAge)