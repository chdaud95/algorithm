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


count_number(150, 266, 427)


#백준 1475 방번호
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


#room_number = input("방번호 입력해줘")
#set_room_number(room_number)


#백준 3273번
def sum_number(length: int, num_list: list, result: int):
  sum_list = [0 for i in range(max(num_list))]
  count = 0
  for i in num_list:
    val = result - i
    if sum_list[val - 1] == 0:
      sum_list[i - 1] = 1
    else:
      count += 1
  print("백준 3273번 답 {}".format(count))


sum_number(9, [5, 12, 7, 10, 9, 1, 2, 3, 11], 13)


#백준 1080번
def count_contain_number(contain_list: list, contain_number:int):
  count = 0
  for i in contain_list:
    if i == contain_number:
      count += 1

  print("백준 1080번 답 {}".format(count))
