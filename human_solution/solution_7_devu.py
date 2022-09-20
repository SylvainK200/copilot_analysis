for t in range(int(input())):
  n, k = list(map(int, input().split()))
  buckets = list(map(int, input().split()))
  ops = 0
  for b in buckets:
    if k > b:
      ops += k - b
    elif b % k > k / 2:
      ops += k - b % k
    else:
      ops += b % k
  print(ops)
