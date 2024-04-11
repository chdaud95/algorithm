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
    if prev_node == self.dummy : return None
    else: return prev_node

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

list.addAfter(second_node,123)
list.display()

#백준 1406 에디터 문제

"""
  손코딩 문제 
  1. 원형 연결 리스트 내의 임의의 노드 하나가 주어졌을 때 해당 List 길이를
  효율적으로 구하는 방법
    -> 동일한 노드가 나올때 까지 순회하면 된다
  2.
"""
