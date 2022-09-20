#!/usr/bin/python
# coding=utf8
import sys
import time

def main():
    data = sys.stdin
    nb = int(data.readline())
    #nb = 16
    for icase in range(nb):
        k, string = data.readline().strip().split()
        #k, string = icase + 1, ""
        k = int(k)
        letters = 2 ** k
        #while(len(string) < letters):
        #    from string import ascii_lowercase
        #    import random
        #    string += random.choice(ascii_lowercase)
        #print string

        # brute force
        res = ''
        for i in range(letters):
            bi = bin(i)[2:]
            bi = '0' * (k - len(bi)) + bi
            bi = bi[::-1]
            v = int(bi, 2)
            res += string[v]

        print(res)


if __name__ == "__main__":
    main()
