import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
sequence_list = []
visited_list = {}

def backTracking(depth):
  if depth == M:
    temp = ' '.join(map(str, sequence_list))
    if temp not in visited_list:
      visited_list[temp] = 1
      print(temp)
    return
  
  for number in numbers:
    if sequence_list and sequence_list[-1] > number:
      continue
    
    sequence_list.append(number)
    backTracking(depth + 1)
    sequence_list.pop()

backTracking(0)
