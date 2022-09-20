for t in range(int(input())):
  N, M = list(map(int, input().split()))
  matrix = []
  for _ in range(N):
    matrix.append(input())
  popular = {}
  for girl in range(M):
    for boy in range(N):
      if matrix[boy][girl] == '1':
        popular[girl] = popular.get(girl, 0) + 1
  print(sum([(n * (n - 1)) / 2 for n in list(popular.values()) if n > 1]))