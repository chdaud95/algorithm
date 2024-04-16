"""
  백트래킹:
    현재 상태에서 가능한 모든 후보군을 따라 들어가며 탐색하는 알고리즘
"""
import io

# 백준 15649
# def func_n1(k:int):
#   if k == m:
#     string_buffer = io.StringIO()
#     for i in range(m):
#       string_buffer.write(str(arr[i])+" ")
#     print(string_buffer.getvalue().strip())
#     return
#
#   i = 1
#   for _ in range(n):
#     if is_used[i] == False:
#       arr[k] = i
#       is_used[i] = True
#       func_n1(k+1)
#       is_used[i] = False
#     i += 1
# n,m = map(int,input().split())
# arr = [0 for _ in range(10)]
# is_used = [False for _ in range(10)]
# func_n1(0)

# 백준 9663

def set_queen(cur:int):
  global cnt
  if cur == len:
    cnt += 1
    return

  for i in range(len):
    if is_used1[i] or is_used2[cur+i] or is_used3[cur-i+len-1]:
      continue
    is_used1[i] = True
    is_used2[cur+i] = True
    is_used3[cur-i+len-1] = True
    set_queen(cur+1)
    is_used1[i] = False
    is_used2[cur + i] = False
    is_used3[cur - i + len - 1] = False
cnt = 0
len = int(input())
is_used1 = [False for _ in range(40)]
is_used2 = [False for _ in range(40)]
is_used3 = [False for _ in range(40)]
set_queen(0)
print(cnt)
