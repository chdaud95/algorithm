import sys


def s_6198():
  n = int(input())
  buildings = []
  stack = []
  count = 0
  for i in range(n):
    buildings.append(int(input()))

  for item in buildings:

    while stack and stack[-1] <= item:
      stack.pop()

    stack.append(item)
    count += len(stack) - 1

  print(count)

s_6198()
