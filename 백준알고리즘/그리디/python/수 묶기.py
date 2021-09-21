import sys
from types import resolve_bases
input = sys.stdin.readline

N = int(input())
negative =[]
positive = []

for _ in range(N):
  num = int(input())
  if num <= 0:
    negative.append(num)
  else:
    positive.append(num)

res = 0
negative.sort()
positive.sort(reverse=True)

while len(negative) > 1:
  n1, n2 = negative.pop(0), negative.pop(0)
  res += n1 * n2

if len(negative) == 1:
  res += negative[0]

while len(positive) > 1:
  n1, n2 = positive.pop(0), positive.pop(0)
  if n1 == 1 or n2 == 1:
    res += n1 + n2
  else:
    res += n1 * n2

if len(positive) == 1:
  res += positive[0]

print(res)