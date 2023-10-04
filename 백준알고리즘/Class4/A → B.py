from collections import deque
import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

A, B = map(int, input().split())
answer = 0

while B != A:
  answer += 1
  temp = B
  
  if B % 10 == 1:
    B //= 10
  elif B % 2 == 0:
    B //= 2
  
  if temp == B:
    print(-1)
    break
if B == A:
  print(answer + 1)