import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
sequence_list = []

def backTracking(depth):
  if depth == M:
    print(*sequence_list)
    return
  
  for number in numbers:
    if sequence_list and sequence_list[-1] > number:
      continue
    
    sequence_list.append(number)
    backTracking(depth + 1)
    sequence_list.pop()
  
backTracking(0)