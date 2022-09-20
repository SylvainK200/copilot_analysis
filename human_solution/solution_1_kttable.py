for t in range(int(input())):
  n = int(input())
  clock = [0] + list(map(int, input().split()))
  required = list(map(int, input().split()))
  fit = 0
  for i in range(n):
    if clock[i + 1] - clock[i] >= required[i]:
      fit += 1
  print(fit)