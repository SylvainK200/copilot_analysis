# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 12:29:47 2016

@author: matteoarno
"""

import sys

data = sys.stdin.readlines()
t = int(data.pop(0))

for i in range(t):
    a, b, c = (list(map(int, data.pop(0).split(' '))))
    if (a+b+c == 180) and (all(x > 0 for x in [a,b,c])):
        print('YES')
    else:
        print('NO')
    