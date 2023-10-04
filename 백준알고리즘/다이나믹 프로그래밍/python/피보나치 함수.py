import sys
input = sys.stdin.readline

zero = [1, 0, 1]
one = [0, 1, 1]


def solution(n):
  length = len(zero)
  if n >= length:
    for i in range(length, n + 1):
      zero.append(zero[i - 2] + zero[i - 1])
      one.append(one[i - 2] + one[i - 1])
  
  return (zero[n], one[n])


for _ in range(int(input())):
  n = int(input())
  print(*solution(n))