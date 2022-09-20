for t in range(int(input())):
  len_n, len_k = list(map(int, input().split()))
  n = input().split()
  k = []
  for _ in range(len_k):
    for l in (input().split()[1:]):
      k.append(l)
  for i in n:
    if i in k:
      print('YES', end=' ')
    else:
      print('NO', end=' ')
  print()