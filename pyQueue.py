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
