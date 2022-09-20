# cook your code here
for testcases in range(int(input() ) ) :
    N=int(input())
    S=input()
    print(N-max(S.count('R'), S.count('G'),S.count('B')))