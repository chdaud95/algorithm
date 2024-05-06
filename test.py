import sys
xy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def s_1012(x, y):
  queue = []
  graph[x][y] = 0
  queue.append((x, y))

  while queue:
    cur_x, cur_y = queue.pop(0)
    for i in range(4):
      nx = cur_x + xy[i][0]
      ny = cur_y + xy[i][1]
      if nx < 0 or nx >= m or ny < 0 or ny >= n: continue
      if graph[nx][ny] != 1: continue
      graph[nx][ny] = 0
      queue.append((nx, ny))


t = int(sys.stdin.readline())
for _ in range(t):
  count = 0
  n, m, k = map(int, sys.stdin.readline().split())
  graph = [[0 for _ in range(n)] for _ in range(m)]
  for i in range(k):
    a, b = map(int, sys.stdin.readline().split())
    graph[b][a] = 1

  for i in range(m):
    for j in range(n):
      if graph[i][j] == 1:
        s_1012(i, j)
        count += 1
  print(count)
