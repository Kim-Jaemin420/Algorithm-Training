import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [False] * N
sequence_list = []

def backTracking(depth):
  if depth == M:
    print(*sequence_list)
  
  for i in range(N):
    if not visited[i]:
      if sequence_list and sequence_list[-1] > i + 1:
        continue
      visited[i] = True
      sequence_list.append(i + 1)
      backTracking(depth + 1)
      visited[i] = False
      sequence_list.pop()
      
backTracking(0)