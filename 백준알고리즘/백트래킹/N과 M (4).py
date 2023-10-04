import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sequence_list = []

def backTracking(depth):
  if depth == M:
    print(*sequence_list)
    return
  
  for i in range(1, N + 1):
    if sequence_list and sequence_list[-1] > i:
      continue
    
    sequence_list.append(i)
    backTracking(depth + 1)
    sequence_list.pop()

backTracking(0)