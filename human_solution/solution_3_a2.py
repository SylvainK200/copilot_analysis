#!/usr/bin/env python
#  johnnyAndBeanstalk.py
#
#  input: int t (num cases, 1<= t <= 20)
#           int k (num levels of beanstalk, 1<= k <=10^6)
#             ints k (num leaves of beanstalk, spaced seperated, <10^6)
#
#  output:  "Yes" or "No" for each case
#
#  rule of growth: for each level, stem into 1 leaf or branch into 2 stem

from sys import stdin


def main():
    num_cases = int(stdin.readline())
    for i in range(num_cases):
        if case():
            print("Yes")
        else:
            print("No")

def case():
    num_levels = int(stdin.readline())
    leaves = list(map(int, stdin.readline().split()))
    num_stem = 0.5
    for i in range(len(leaves)):
        num_stem = (num_stem * 2) - leaves[i]
    return num_stem == 0
    

if __name__ == "__main__":
    main()
