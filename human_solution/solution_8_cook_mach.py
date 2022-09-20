for t in range(int(input())):
  a, b = list(map(int, input().split()))
  ops = 0
  while a > b or a & a - 1:
    a >>= 1
    ops += 1
  while a != b:
    a <<= 1
    ops += 1
  print(ops)