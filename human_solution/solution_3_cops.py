for t in range(int(input())):
  block = list(range(1, 101))
  M, x, y = list(map(int, input().split()))
  sweep = x * y
  for m in map(int, input().split()):
    lo_sweep = max(m - sweep-1, 0)
    hi_sweep = min(m + sweep, 100)
    tblock = list(range(1, 101))
    # print '%d to %d covered' % (tblock[lo_sweep:hi_sweep][0], tblock[lo_sweep:hi_sweep][-1])
    for i in tblock[lo_sweep:hi_sweep]:
      if i in block:
        block.remove(i)
    # print block
    if len(tblock) == 0:
      print(0)
      break
  else:
    print(len(block))
