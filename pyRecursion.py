"""
  재귀함수
    - 함수의 인자로 어떤 것을 받고 어디까지 계산한 후 자기 자신에게 넘겨줄지 명화학게 정해야함
    - 모든 재귀 함수는 반복문만으로 동일한 동작을 하는 함수를 만들 수 있음
    - 재귀는 반복문으로 구현했을 때에 비해 코드가 간결하지만 메모리/시간에서는 손해를봄
    - 한 함수가 자기 자신을 여러 번 호출하게 되면 비효율적일 수 있음(동일한 연산을 여러번실행)
    - 재귀함수가 자기 자신을 부를 때 스택 영역에 계속 누적이 됨
"""


# 백준 1629
def get_mod(a, b, c):
  if b == 1:
    return a % c
  if b % 2 == 0:
    return (get_mod(a, b // 2, c) ** 2) % c
  return (get_mod(a, b // 2, c) ** 2 * a) % c


# l,m,n = map(int,input().split())
# print(get_mod(l,m,n))

# 백준 1914
def hanoi(n, a, b):
  if n == 1:
    print(a, b)
    return
  hanoi(n - 1, a, 6 - a - b)
  print(a, b)
  hanoi(n - 1, 6 - a - b, b)


# n = int(input())
# print(2**n - 1)
# if n <= 20: hanoi(n, 1, 3)

# 백준 1074번
def func_z(length, r, c):
  if length == 0:
    return 0
  half = 2 ** (length - 1)
  if r < half and c < half:
    return func_z(length - 1, r, c)
  elif r < half and c >= half:
    return half*half + func_z(length - 1, r, c)
  elif r >= half and c < half:
    return 2 * half*half + func_z(length - 1, r, c)
  return 3 * half*half + func_z(length - 1, r, c)


# l, n, m = map(int, input().split())
# print(func_z(l, n, m))
