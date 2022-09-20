#!/bin/python


class Wallet():
    def __init__(self, bnum):
        self.bnum = bnum
        self.blist = []

    def addb(self, value):
        self.blist.append(value)

    def answerMuggler(self, value):
        if sum(self.blist) < value:
            print('No')
            return

        self.blist.sort(reverse=True)
        
        k = 0 ; cases =0
        avail = 0
        while avail != value and k < self.bnum:
            l = k
            while avail != value and l < self.bnum:
                i = l + 1
                avail = self.blist[k]
                while avail < value and i < self.bnum:
                    # print(k, l, i, avail, self.blist[i])
                    avail += self.blist[i]
                    if avail > value and i < self.bnum:
                        avail -= self.blist[i]
                    # print(avail)
                    cases += 1
                    i += 1
                l += 1
            k += 1
#        print(cases    )
        if avail == value:
            print('Yes')
            return
        else:
            print('No')
            return


import sys
numberOfWallets = int(sys.stdin.readline())

for w in range(numberOfWallets):
    nban, smugglerWants = sys.stdin.readline().split()
    w = Wallet(int(nban))
    for b  in range(int(nban)):
        b = sys.stdin.readline()
        w.addb(int(b))
    w.answerMuggler(int(smugglerWants))
