"""
  수식의 괄호 쌍, 전위/중위/후위 표기법, DFS, Flood Fill 등에서 사용
"""
import re


class Stack:
  def __init__(self):
    self.stack = []

  def push(self, val):
    self.stack.append(val)

  def pop(self):
    if self.isEmpty(): return

    return self.stack.pop()

  def top(self):
    if self.isEmpty(): return
    return self.stack[-1]

  def isEmpty(self):
    return len(self.stack) == 0

  def size(self):
    return len(self.stack)


# 백준 4949번
def only_bracket(text: str) -> str:
  return re.sub(r'[^\[\]()]+', '', text)


def check_balance(text: str) -> str:
  answer = 'yes'
  text = only_bracket(text)
  stack = Stack()

  for i in text:
    if i == '[' or i == '(':
      stack.push(i)
    elif i == ']':
      if stack.pop() != '[':
        answer = 'no'
        break
    elif i == ')':
      if stack.pop() != '(':
        answer = 'no'
        break
  if (stack.isEmpty() == False): answer = 'no'
  return answer


# while True:
#   str = input()
#   if str == '.':
#     break
#   else:
#     print(check_balance(str))

# 백준 10799
# str = input()
# stick_stack = Stack()
# stick_count = 0
# for i in range(len(str)):
#   if str[i] == '(':
#     stick_stack.push(str[i])
#   else:
#     if str[i - 1] == '(':  # 레이저
#       stick_stack.pop()
#       stick_count += stick_stack.size()
#     else:
#       stick_stack.pop()
#       stick_count += 1
#
# print(stick_count)

# 백준 2504
stack = []  # 스택
res = 1  # result에 더해주기 전 임시 변수
result = 0  # 결과 변수
p = list(input())  # 입력값

# 1~4번째 과정 시작
for i in range(len(p)):
  if p[i] == '(':
    res *= 2
    stack.append(p[i])

  elif p[i] == '[':
    res *= 3
    stack.append(p[i])

  elif p[i] == ')':
    if not stack or stack[-1] != '(':
      result = 0
      break
    if p[i - 1] == '(': result += res
    res //= 2
    stack.pop()

  elif p[i] == ']':
    if not stack or stack[-1] != '[':
      result = 0
      break
    if p[i - 1] == '[': result += res
    res //= 3
    stack.pop()

# 결과 출력
if stack:
  print(0)
else:
  print(result)

