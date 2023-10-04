import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
visited = [False] * N
visited_list = []
sequence_list = []

def backTracking(depth):
  if depth == M:
    temp = ' '.join(map(str, sequence_list))
    if temp not in visited_list:
      visited_list.append(temp)
      print(temp)
    return
  
  for i in range(N):
    if visited[i] or sequence_list and numbers[i] < sequence_list[-1]:
      continue
    
    sequence_list.append(numbers[i])
    visited[i] = True
    backTracking(depth + 1)
    sequence_list.pop()
    visited[i] = False


backTracking(0)