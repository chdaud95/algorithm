"""
  배열의 성질
  1. O(1)에 k번째 원소를 확인/변경 가능
  1-1 임의의 위치에 원소를 추가/삭제 = O(N)
  2. 추가적으로 소모되는 메모리의 양(=overhead)가 거의 없음
  3. Cache hit rate가 높음
  4. 메모리 상에 연속한 구간을 잡아야 해서 할당에 제약이 걸림
"""
import sys


def insert(index: int, num: int, arr: list) -> None:
  length = len(arr)
  i = length
  while i >= index:
    if i == length: arr.append(0)
    arr[i] = arr[i - 1]
    i = i - 1
  arr[index] = num


def delete(index: int, arr: list) -> None:
  length = len(arr)
  i = index
  while i < length - 1:
    arr[i] = arr[i + 1]
    i = i + 1
  del (arr[length - 1])


list = list(range(10))
insert(3, 100, list)
delete(3, list)


def sum_hundred(arr: list) -> int:
  compare_arr = [0 for i in range(100)]
  flag = 0
  for i in arr:
    num = 100 - i
    if compare_arr[num - 1] == 0:
      compare_arr[i - 1] = 1
    elif compare_arr[num - 1] == 1:
      flag = 1

  # print(flag)


# sum_hundred([1, 52, 48])
# sum_hundred([50, 42])
# sum_hundred([4, 13, 63, 87])

# 백준 10808 알파벳 개수
arr = [0 for i in range(26)]


def count_alphabet(arr: list, alphabet: str) -> None:
  for i in alphabet:
    index = ord(i) % 97
    arr[index] = arr[index] + 1
  print(" ".join(str(s) for s in arr))


# text = input()
# count_alphabet(arr, text)


# 백준 2577 숫자의 개수
def count_number(A: int, B: int, C: int) -> None:
  result = str(A * B * C)
  arr = [0 for i in range(10)]
  for i in result:
    arr[int(i)] = arr[int(i)] + 1
  for i in arr:
    print(i)


# three_number = [input() for _ in range(3)]
# count_number(int(three_number[0]), int(three_number[1]), int(three_number[2]))


# 백준 1475 방번호
def set_room_number(number: str) -> None:
  arr = [0 for i in range(10)]

  for i in number:
    if i == "9" or i == "6":
      six = arr[int(6)]
      nine = arr[int(9)]
      if six < nine:
        arr[6] = arr[6] + 1
      elif six > nine:
        arr[9] = arr[9] + 1
      else:
        arr[int(i)] = arr[int(i)] + 1
    else:
      arr[int(i)] = arr[int(i)] + 1

  print(max(arr))


# room_number = input()
# set_room_number(room_number)


# 백준 3273번
def sum_number(length: int, num_list: list, result: int):
  num_list.sort()
  start, end = 0, length - 1
  count = 0
  while start < end:
    sum = num_list[start] + num_list[end]
    if sum < result:
      start += 1
    elif sum > result:
      end -= 1
    else:
      start += 1
      count += 1
  print(count)


# N = int(input())
# arr = list(map(int, input().split()))
# X = int(input())
# sum_number(N, arr, X)


# 백준 13300번
def assign_room(students: int, limit: int, student_arr: list):
  room_count = 0
  arr = [[0 for j in range(6)] for i in range(2)]
  for i in range(students):
    sex = student_arr[i][0]
    grade = student_arr[i][1]
    arr[sex][grade - 1] = arr[sex][grade - 1] + 1

  for ir in arr:
    for j in ir:
      room_count += j // limit
      if j % limit != 0:
        room_count += 1

  print(room_count)


# N, K = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(N)]
# assign_room(N, K, a)

# 백준 11328번
def is_strfry(text: str, strfry_text:str):
  for l in set(text):
    if text.count(l) != strfry_text.count(l):
      print("Impossible")
      break
  else:
    print("Possible")

# N = int(input())
# for i in range(1, N+1):
#   str, convert_str = input().split()
#   is_strfry(str,convert_str)

# 백준 1919
def anagram(first_text: str, second_text: str):
  arr = [0]*26
  a = list(first_text)
  for i in list(first_text):
    arr[ord(i)-97] += 1

  for i in list(second_text):
    arr[ord(i)-97] -= 1
  count = 0
  for i in arr:
    count += abs(i)
  print(count)

A = input()
B = input()
anagram(A,B)



