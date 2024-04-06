"""
  N 의 크기          허용 시간복잡도
  N <= 11               O(N!)
  N <= 25               O(2^n)
  N <= 100              O(N^4)
  N <= 500              O(N^3)
  N <= 3000             O(N^2 * logN)
  N <= 5000             O(N^2)
  N <= 1000000          O(N*logN)
  N <= 10000000         O(N)
  그 이상                O(logN),O(1)

  ** 메모리가 512MB = 1.2억개의 int를 선언가능

"""

"""
  실수 자료형의 최소값과 최대값
  IEEE-754 format 확인
"""
import math


# 문제 1 N <= 100000 3의 배수 이거나 5의 배수인 수
def func1(number: int):
  count = 0
  for i in range(1, number + 1):
    if i % 3 == 0 or i % 5 == 0:
      count = count + i
  print(count)


func1(16)
func1(34567)
func1(27639)


# 문제 2 길이 N 의 int 배열 arr에서 합이 100인 서로다른 위치의 두 원소가 존재하면 1 아니면 0을 반환 0<= arr[i] <=100 , n <=1000
def func2(arr: list) -> int:
  length = len(arr)
  flag = 0
  for i in range(length):
    for j in range(i + 1, length):
      if arr[i] + arr[j] == 100:
        flag = 1
        break
  return flag


print(func2([1, 52, 48]))
print(func2([50, 42]))
print(func2([4, 13, 63, 87]))


# 문제3 N이 제곱수 이면 1을 반환하고 제곱수가 아니면 0을 반환하는 함수 N <= 1000000000
def func3(number):
  for i in range(1, number + 1):
    if i * i > number: break
    if i * i == number: return 1
    i = i + 1
    i = i * i
  return 0

  # answer = 0
  # sqrt_num = math.sqrt(number)
  # if float(int(sqrt_num)) == sqrt_num:
  #   answer = 1
  # return answer


print(func3(9))
print(func3(693953651))
print(func3(756580036))


# 문제 4 N 이하의 수 중에서 가장 큰 2의 거듭 제곱수를 반환 하는 함수 N <= 1000000000
def func4(number:int) -> int:
  val = 1
  while 2 * val <= number: val = val * 2;
  return val


print(func4(5))
print(func4(97615282))
print(func4(1024))

# Integer Overflow
def int_func() :
  a = 10
  mod = 1000000007
  for i in range(10):
    print(a)
    a = 10 * a % mod
    print(a)
  return a

print(int_func())

