import sys
from collections import deque


def escape_fire(graph, row, col):
  fire_time = [[-1 for _ in range(col)] for _ in range(row)]
  jihun_time = [[-1 for _ in range(col)] for _ in range(row)]

  fire_graph = [[0 for _ in range(col)] for _ in range(row)]
  jihun_graph = [[0 for _ in range(col)] for _ in range(row)]

  xy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

  queue = deque()
  start_fire = (0, 0)
  start_jihun = (0, 0)
  for i in range(row):
    for j in range(col):
      if graph[i][j] == '#':
        fire_graph[i][j] = 0
        jihun_graph[i][j] = 0
      elif graph[i][j] == '.':
        fire_graph[i][j] = 1
        jihun_graph[i][j] = 1
      elif graph[i][j] == 'J':
        fire_graph[i][j] = 1
        jihun_graph[i][j] = 1
        jihun_time[i][j] = 0
        start_jihun = (i, j)
      elif graph[i][j] == 'F':
        fire_graph[i][j] = 1
        jihun_graph[i][j] = 0
        fire_time[i][j] = 0
        start_fire = (i, j)


  # 불의 전파
  queue.append(start_fire)
  while bool(queue):
    cur_x, cur_y = queue.popleft()
    for i in range(4):
      nx = cur_x + xy[i][0]
      ny = cur_y + xy[i][1]
      if nx < 0 or nx >= row or ny < 0 or ny >= col: continue
      if fire_graph[nx][ny] != 1 or fire_time[nx][ny] >= 0: continue
      fire_time[nx][ny] = fire_time[cur_x][cur_y] + 1
      queue.append((nx, ny))

  for i in range(row):
    print(fire_time[i])

  # 지훈이 이동
  queue.append(start_jihun)
  while bool(queue):
    cur_x, cur_y = queue.popleft()
    for i in range(4):
      nx = cur_x + xy[i][0]
      ny = cur_y + xy[i][1]
      if nx < 0 or nx >= row or ny < 0 or ny >= col:
        print(jihun_time[cur_x][cur_y]+1)
        return
      if jihun_graph[nx][ny] != 1 or jihun_time[nx][ny] > 0: continue
      if fire_time[nx][ny] != -1 and fire_time[nx][ny] <= jihun_time[cur_x][cur_y]+1: continue
      jihun_time[nx][ny] = jihun_time[cur_x][cur_y] + 1
      queue.append((nx, ny))

  print("IMPOSSIBLE")


n, m = map(int, input().split())
mp = [list(input()) for _ in range(n)]
escape_fire(mp, n, m)
