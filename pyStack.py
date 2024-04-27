"""
  수식의 괄호 쌍, 전위/중위/후위 표기법, DFS, Flood Fill 등에서 사용
"""
import re
import sys


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
# stack = []  # 스택
# res = 1  # result에 더해주기 전 임시 변수
# result = 0  # 결과 변수
# p = list(input())  # 입력값
#
# # 1~4번째 과정 시작
# for i in range(len(p)):
#   if p[i] == '(':
#     res *= 2
#     stack.append(p[i])
#
#   elif p[i] == '[':
#     res *= 3
#     stack.append(p[i])
#
#   elif p[i] == ')':
#     if not stack or stack[-1] != '(':
#       result = 0
#       break
#     if p[i - 1] == '(': result += res
#     res //= 2
#     stack.pop()
#
#   elif p[i] == ']':
#     if not stack or stack[-1] != '[':
#       result = 0
#       break
#     if p[i - 1] == '[': result += res
#     res //= 3
#     stack.pop()
#
# # 결과 출력
# if stack:
#   print(0)
# else:
#   print(result)

# 백준 9012
# def check_vps(parenthesis: str):
#   arr = []
#   answer = "YES"
#   for i in parenthesis:
#     if i == "(":
#       arr.append(i)
#     else:
#       if not bool(arr):
#         answer = "NO"
#         break
#       check = arr.pop()
#       if check == ")":
#         answer = "NO"
#   if arr: answer = "NO"
#   print(answer)
#
#
# n = int(input())
# for _ in range(n):
#   text = input()
#   check_vps(text)

# 백준 2504
# def value_parenthesis(text: str):
#   arr = []
#   tmp = 1
#   answer = 0
#   for i in range(len(text)):
#     if text[i] == '(':
#       arr.append(text[i])
#       tmp *= 2
#     elif text[i] == '[':
#       arr.append(text[i])
#       tmp *= 3
#     elif text[i] == ')':
#       if not arr or arr[-1] == '[':
#         answer = 0
#         break
#       if text[i-1] == '(':
#         answer += tmp
#       arr.pop()
#       tmp //= 2
#     elif text[i] == ']':
#       if not arr or arr[-1] == '(':
#         answer = 0
#         break
#       if text[i-1] == '[':
#         answer += tmp
#       arr.pop()
#       tmp //= 3
#   if arr : answer = 0
#   print(answer)
#
# n = input()
# value_parenthesis(n)

#백준 10773

# def sum_num():
#   n = int(input())
#   stack = []
#   for _ in range(n):
#     num = int(sys.stdin.readline())
#     if num == 0:
#       stack.pop()
#     else:
#       stack.append(num)
#   print(sum(stack))
#
# sum_num()

#백준 1874
# def s_1817():
#   n = int(input())
#   stack = []
#   answer = []
#   now = 1
#   for i in range(n):
#     num = int(input())
#     while num >= now:
#       stack.append(now)
#       answer.append("+")
#       now += 1
#
#     if stack[-1] == num:
#       stack.pop()
#       answer.append("-")
#     else:
#       print("NO")
#       return
#   for i in answer:
#     print(i)
#
# s_1817()
