import sys
# input = sys.stdin.readline

sys.stdin = open('input.txt', 'r')

T = int(input())

for _ in range(T):
  A, B = map(int, input().split())
  sum = 0
  
  for i in range(2, A):
    if A % i == 0:
      sum += i
      
  print('yes' if sum == B else 'no')