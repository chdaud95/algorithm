class Deque:
  def __init__(self,max_size):
    self.deque = [None]*max_size
    self.head = max_size - 1
    self.tail = max_size - 1

  def front_push(self,val):
    if self.isFull():
      return
    self.head = self.getFrontPos(self.head)
    self.deque[self.head] = val

  def back_push(self,val):
    if self.isFull():
      return
    self.tail = self.getBackPos(self.tail)
    self.deque[self.tail] = val
  def front_pop(self):
    if self.isEmpty():
      return



  def back_pop(self):
    if self.isEmpty():
      return

  def getFrontPos(self,pos):
    if pos - 1 < 0:
      return len(self.deque) - 1
    else:
      return pos - 1

  def getBackPos(self,pos):
    if pos == len(self.deque) - 1:
      return 0
    else:
      return pos + 1

  def isEmpty(self):
    if self.head == self.tail:
      return True
    else:
      return False

  def isFull(self):
    if self.getBackPos(self.tail) == self.head:
      return True
    else:
      return False

# 백준 1021
# from collections import deque
# n,m = map(int,input().split())
# arr = deque([i for i in range(1,n+1)])
# index = list(map(int,input().split()))
# count = 0
# for num in index:
#   while 1:
#     if arr[0] == num:
#       arr.popleft()
#       break;
#     else:
#       if arr.index(num) <= len(arr)//2:
#         arr.rotate(-1)
#         count += 1
#       else:
#         arr.rotate(1)
#         count += 1
# print(count)

# 백준 5430