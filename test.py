import sys
array=list(range(1,31))
for _ in range(28):
  n=int(sys.stdin.readline())
  array.remove(n)
print(array[0])
print(array[1])