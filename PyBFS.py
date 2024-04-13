"""
  BFS(Breadth-First-Search)
  : 다차원 배열에서 각 칸을 방문할 때 너비를 우선으로 방문하는 알고리즘
    그래프라는 자료구조에서 모든 노드를 방문하기 위한 알고리즘

  1. 시작하는 칸에 큐를 넣고 방문했다는 표시를 남김
  2. 큐에서 원소를 꺼내어 그 칸에 상하좌우로 인접한 칸에 대해 3번을 진행
  3. 해당 칸을 이전에 방문했다면 아무것도 하지 않고, 처음으로 방문했다면 방문했다는 표시를남기고 해당 칸을 큐에 삽입
  4. 큐가 빌 때까지 2번을 반복, 모든 칸이 큐에 1번씩 들어가므로 시간복잡도는 칸이 N개일 때 O(N)

  x 가 열 y 가 행
"""
import sys
from collections import deque


# 백준 1926번
def print_analyze(graph, row, col):
  count_print = 0
  max_print = 0
  dx = [1, 0, -1, 0]
  dy = [0, 1, 0, -1]
  queue = deque()
  visit = [[0 for j in range(col)] for i in range(row)]

  for i in range(row):
    for j in range(col):
      if graph[i][j] == 0 or bool(visit[i][j]): continue  # 시작점 찾기
      # 시작위치 방문 표시
      count_print += 1
      visit[i][j] = 1
      queue.append((i, j))
      area = 1
      while (bool(queue)):
        cur_x, cur_y = queue.popleft()
        for z in range(4):
          nx = cur_x + dx[z]
          ny = cur_y + dy[z]
          if nx < 0 or nx >= row or ny < 0 or ny >= col: continue  # 범위를 벗어나면 안됨
          if bool(visit[nx][ny] or graph[nx][ny] != 1): continue  # 방문했거나 탐색범위에서 벗어나면 안됨
          visit[nx][ny] = 1
          queue.append((nx, ny))
          area += 1

      max_print = max(max_print, area)
  print(count_print)
  print(max_print)


# n, m = map(int, sys.stdin.readline().strip().split())
# mp = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# print_analyze(mp, n, m)

# 백준 2178
def search_root(graph, row, col):
  xy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
  queue = deque()

  distance = [[-1 for j in range(col)] for i in range(row)]
  distance[0][0] = 0
  queue.append((0, 0))
  while (bool(queue)):
    cur_x, cur_y = queue.popleft()
    cur_dis = distance[cur_x][cur_y]
    for i in range(4):
      x, y = xy[i]
      nx = cur_x + x
      ny = cur_y + y
      if nx < 0 or nx >= row or ny < 0 or ny >= col: continue
      if graph[nx][ny] == 0 or distance[nx][ny] != -1: continue
      distance[nx][ny] = cur_dis + 1
      queue.append((nx, ny))

  print(distance[row - 1][col - 1] + 1)


# n, m = map(int, sys.stdin.readline().strip().split())
# mp = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
# search_root(mp, n, m)

# 백준 7576
def grow_tomatoes(graph, row, col):
  start_queue = deque()  # 익은 토마토가 있는 칸
  no_queue = deque()  # 토마토가 없는 칸
  distance = [[0 for j in range(col)] for i in range(row)]
  xy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

  for i in range(row):
    for j in range(col):
      if graph[i][j] == 1:
        start_queue.append((i, j))
      elif graph[i][j] == -1:
        no_queue.append((i, j))
      else:
        distance[i][j] = -1
  if len(start_queue) + len(no_queue) >= row * col:
    # 익어야할 토마토가 없을경우 0
    print(0)
    return

  for i in range(len(start_queue)):
    while bool(start_queue):
      cur_x, cur_y = start_queue.popleft()
      for z in range(4):
        x, y = xy[z]
        nx = cur_x + x
        ny = cur_y + y
        if nx < 0 or nx >= row or ny < 0 or ny >= col: continue
        if distance[nx][ny] >= 0: continue
        distance[nx][ny] = distance[cur_x][cur_y] + 1
        start_queue.append((nx, ny))

  max_val = 0
  for i in range(row):
    for j in range(col):
      if distance[i][j] == -1:
        print(-1)
        return
      max_val = max(max_val, distance[i][j])
  print(max_val)


# m, n = map(int, sys.stdin.readline().strip().split())
# mp = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]
# grow_tomatoes(mp, n, m)


# TODO 백준 7569

# 백준 4179
def escape_fire(graph, row, col):
  visit_fire = [[ 0 for _ in range(col) ] for _ in range(row)]
  distance = [[0 for _ in range(col)] for _ in range(row)]

  jihun_graph = [[0 for _ in range(col)] for _ in range(row)]
  fire_graph = [[0 for _ in range(col)] for _ in range(row)]

  for i in range(row):
    for j in range(col):
      if graph[i][j] == '#':
        jihun_graph[i][j] = 0
        fire_graph[i][j] = 0
      elif graph[i][j] == '.':
        jihun_graph[i][j] = 1
        fire_graph[i][j] = 1
      elif graph[i][j] == 'J':
        fire_graph[i][j] = 1
      elif graph[i][j] == 'F':
        jihun_graph[i][j] = 0

  print(graph)
  print(jihun_graph)
  print(fire_graph)


n, m = map(int, input().split())
mp = [list(input()) for _ in range(n)]
escape_fire(mp, n, m)
