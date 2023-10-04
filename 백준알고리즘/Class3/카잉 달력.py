import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  M, N, x, y = map(int, input().split())
  answer = -1
  
  if x == M * N:
    answer = 1
  
  while x < M * N:
    if x % N == y % N:
      answer = x
      break
    x += M
  
  print(answer)