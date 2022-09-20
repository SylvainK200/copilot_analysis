# -*- coding: utf-8 -*-
__author__ = 'sagar'


def test_fibonnaci():
    fibo_nums = []
    a, b = 0, 1
    fibo_nums.append(a)
    while b < 10**1000:
        a, b = b, a+b
        fibo_nums.append(a)
    return fibo_nums

if __name__=="__main__":
    fibbo = test_fibonnaci()
    t=int(input())
    while(t):
        n=int(input())
        if n in fibbo:
            print("YES")
        else:
            print("NO")
        t-=1