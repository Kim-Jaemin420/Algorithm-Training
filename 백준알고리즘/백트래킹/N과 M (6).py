import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
visited = []
sequence_list = []

def backTracking(depth):
  if depth == M:
    print(*sequence_list)
    return
  
  for number in numbers:
    if number in visited:
      continue
      
    if sequence_list and sequence_list[-1] >= number:
      continue
    
    sequence_list.append(number)
    visited.append(number)
    backTracking(depth + 1)
    sequence_list.pop()
    visited.remove(number)

backTracking(0)