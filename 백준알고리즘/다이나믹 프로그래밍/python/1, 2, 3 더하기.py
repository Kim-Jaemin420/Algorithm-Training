import sys
input = sys.stdin.readline

def solution(n):
  if n == 1:
    return 1
  
  if n == 2:
    return 2

  if n == 3:
    return 4

  if n > 3:
    return solution(n - 3) + solution(n - 2) + solution(n - 1)

for _ in range(int(input())):
  n = int(input())
  print(solution(n))