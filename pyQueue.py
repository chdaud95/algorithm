import sys
class CQueue:
  def __init__(self,max_size):
    self.queue = [None]*max_size
    self.head = 0
    self.tail = 0

  def push(self, val):
    if self.isFull():
      print("꽉찼습니다.")
      return
    self.tail = self.getPos(self.tail)
    self.queue[self.tail] = val

  def pop(self):
    if self.isEmpty():
      print("비었습니다.")
      return
    self.head = self.getPos(self.head)
    return self.queue[self.head]


  def getPos(self, pos) -> int:
    if pos == len(self.queue) - 1:
      return 0
    else:
      return pos + 1

  def isEmpty(self):
    if self.head == self.tail:
      return True
    else:
      return False

  def isFull(self):
    if self.getPos(self.tail) == self.head:
      return True
    else:
      return False

# 원형 큐 테스트
# queue = CQueue(5)
# queue.push(1)
# queue.push(2)
# queue.push(3)
# queue.push(4)
# queue.push(5)
# print(queue.pop())
# print(queue.pop())
# print(queue.pop())
# print(queue.pop())
# print(queue.pop())

# 백준 10845,18258
# from collections import deque
# n = int(sys.stdin.readline().strip())
# que = deque()
#
# for _ in range(n):
#   text_arr = sys.stdin.readline().strip().split()
#   if 'push' == text_arr[0]:
#     que.append(text_arr[1])
#   elif 'pop' in text_arr[0]:
#     if que: print(que.popleft())
#     else: print(-1)
#   elif 'size' in text_arr[0]:
#     print(len(que))
#   elif 'empty' in text_arr[0]:
#     if que:print(0)
#     else: print(1)
#   elif 'front' in text_arr[0]:
#     if que: print(que[0])
#     else: print(-1)
#   elif 'back' in text_arr[0]:
#     if que: print(que[-1])
#     else: print(-1)

# 백준 2164
from collections import deque
n = int(input())
deq = deque([i for i in range(1,n+1)])
for i in range(n):
  value = deq.popleft()
  if not deq:
    print(value)
    break
  else:
    deq.append(deq.popleft())
