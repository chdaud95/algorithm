"""
  배열의 성질
  1. O(1)에 k번째 원소를 확인/변경 가능
  1-1 임의의 위치에 원소를 추가/삭제 = O(N)
  2. 추가적으로 소모되는 메모리의 양(=overhead)가 거의 없음
  3. Cache hit rate가 높음
  4. 메모리 상에 연속한 구간을 잡아야 해서 할당에 제약이 걸림
"""


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
print(list)
delete(3, list);
print(list)


def sum_hundred(arr: list) -> int:
  compare_arr = [0 for i in range(100)]
  flag = 0
  for i in arr:
    num = 100 - i
    if compare_arr[num - 1] == 0:
      compare_arr[i - 1] = 1
    elif compare_arr[num - 1] == 1:
      flag = 1

  print(flag)


sum_hundred([1, 52, 48])
sum_hundred([50, 42])
sum_hundred([4, 13, 63, 87])

# 백준 10808 알파벳 개수
arr = [0 for i in range(26)]


def count_alphabet(arr: list, alphabet: str) -> None:
  for i in alphabet:
    index = ord(i) % 97
    arr[index] = arr[index] + 1
  print(arr)


count_alphabet(arr, 'apprehensive')


# 백준 2577 숫자의 개수
def count_number(A: int, B: int, C: int) -> None:
  result = str(A * B * C)
  arr = [0 for i in range(10)]
  for i in result:
    arr[int(i)] = arr[int(i)] + 1
  for i in arr:
    print(i)
A = input()
B = input()
C = input()
count_number(150,266,427)
