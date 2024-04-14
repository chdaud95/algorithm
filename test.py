import sys
from collections import deque


def find_sibling(subin, sibling):
  col = 100001
  distance = [0 for _ in range(col)]

  queue = deque()
  queue.append(subin)
  while bool(queue):
    cur_x = queue.popleft()
    if cur_x == sibling:
      print(distance[cur_x])
      break
    for nx in (cur_x - 1, cur_x + 1, cur_x * 2):
      if 0 <= nx < col and not distance[nx]:
        distance[nx] = distance[cur_x] + 1
        queue.append(nx)

n, m = map(int, input().split())
find_sibling(n, m)
