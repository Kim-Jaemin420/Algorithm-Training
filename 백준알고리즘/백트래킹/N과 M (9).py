import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
sequence_list = []
visited = [False] * N
visited_dict = {}

def backTracking(depth):
  if depth == M:
    tempt = ' '.join(map(str, sequence_list))
    if tempt not in visited_dict:
      print(tempt)
      visited_dict[tempt] = 1
    return
  
  for index in range(N):
    if visited[index]:
      continue
    sequence_list.append(numbers[index])
    visited[index] = True
    backTracking(depth + 1)
    visited[index] = False
    sequence_list.pop()
    
backTracking(0)