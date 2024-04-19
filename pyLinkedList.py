"""
    1. 연결 리스트
    2. 양뱡향 연결리스트
    3. 원형 연결리스트

                   배열      연결리스트
n번째 원소 접근/변경    O(1)       O(N)
임의 위치에 추가/제거   O(N)       O(1)
메모리 상의 배치       연속       불연속
추가적으로 필요한공간    -          O(N)
(Overhead)
"""


class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None
    self.prev = None


class BiLinkedList:
  def __init__(self):
    self.dummy = Node()
    self.size = 0

  def addAtHead(self, val):
    node = Node(val)
    node.next = self.dummy.next

    if self.dummy.next is not None:
      self.dummy.next.prev = node

    self.dummy.next = node
    node.prev = self.dummy
    self.size += 1
    return node

  def addAfter(self, node, val):
    if node is None:
      return self.addAtHead(val)

    newNode = Node(val)
    newNode.next = node.next
    if node.next is not None:
      node.next.prev = newNode

    newNode.prev = node
    node.next = newNode

    self.size += 1

    return newNode

  def deleteAtNode(self, node):
    if node is None:
      return None

    prev_node = node.prev
    next_node = node.next

    prev_node.next = next_node
    next_node.prev = prev_node

    self.size -= 1
    if prev_node == self.dummy:
      return None
    else:
      return prev_node

  def getCount(self):
    return self.size

  def display(self):
    node = self.dummy.next
    while node is not None:
      print(node.data, end=" ")
      node = node.next


list = BiLinkedList()
first_node = list.addAtHead(1)
second_node = list.addAtHead(2)
third_node = list.addAtHead(3)
print(list.getCount())

after_node = list.addAfter(None, 100)
prev_node = list.deleteAtNode(after_node)
list.deleteAtNode(prev_node)
list.display()

list.addAfter(second_node, 123)
list.display()


# 에디터 링크드리스트
class EditorLinkedList:
  def __init__(self):
    self.dummy = Node()
    self.current = self.dummy
    self.size = 0

  def print_editor(self):
    print_text = []
    node = self.dummy.next
    while node is not None:
      print_text.append(str(node.data))
      node = node.next
    print(''.join(print_text))

  def add_cursor(self, value: str):
    node = Node(value)

    # 커서가 중간에 있을 경우 앞에 텍스트와 연결
    if self.current.next is not None:
      node.next = self.current.next
      self.current.next.prev = node

    # 커서앞에 텍스트 입력
    self.current.next = node
    node.prev = self.current

    self.current = node
    self.size += 1

  def move_cursor(self, cursor: str):
    if cursor == '': return
    if cursor == 'L':
      if self.current.prev is not None:
        self.current = self.current.prev
    elif cursor == "D":
      if self.current.next is not None:
        self.current = self.current.next

  def delete_cursor(self):
    if self.size == 0 or self.current.prev is None: return
    self.current.prev.next = self.current.next
    if self.current.next is not None:
      self.current.next.prev = self.current.prev

    self.current = self.current.prev


# 백준 1406 에디터 문제
def editor(press: list):
  if press[0] == 'P':
    list.add_cursor(press[1])
  elif press[0] == 'B':
    list.delete_cursor()
  else:
    list.move_cursor(press[0])


list = EditorLinkedList()
edit_text = input()
for i in edit_text:
  list.add_cursor(i)
n = int(input())
for _ in range(n):
  editor(input().split())
list.print_editor()

# 다른풀이
# left = [input()]
# right = []
# n = int(input())
# for _ in range(n):
#   a = input()
#   if a[0] == "L" and left:
#       right.append(left.pop())
#   elif a[0] == "D" and right:
#       left.append(right.pop())
#   elif a[0] == "B" and left:
#       left.pop()
#   elif a[0] == "P":
#     left.append(a[-1])
# print("".join(left),end='')
# print("".join(right[::-1]))

# 백준 5397
# import sys
# t = int(input())
# for _ in range(t):
#   left = []
#   right = []
#   password = sys.stdin.readline().strip()
#   for i in password:
#     if i == '-' :
#       if left :
#         left.pop()
#     elif i == '<':
#       if left :
#         right.append(left.pop())
#     elif i == '>':
#       if right:
#         left.append(right.pop())
#     else:
#       left.append(i)
#   print(''.join(left),end='')
#   print(''.join(reversed(right)))

# 백준 1158
# from collections import deque
# people = deque()
# remove = []
# n, m = map(int, input().split())
# for i in range(1,n+1): people.append(i)
# while people:
#   for _ in range(m-1):
#     people.append(people.popleft())
#   remove.append(people.popleft())
#
# print(str(remove).replace("[","<").replace("]",">"))

# n,k=map(int,input().split())
# *s,=range(1,n+1)
# t=[]
# i=0
# while s:
#     i=(i+k-1)%len(s)
#     t+=[s.pop(i)]
# print('<'+', '.join(map(str,t))+'>')