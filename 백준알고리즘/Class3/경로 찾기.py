from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = { i + 1 : [] for i in range(N) }
answer = [[0] * N for _ in range(N)]

for i in range(1, N + 1):
  linked = list(map(int, input().split()))
  for j in range(N):
    if linked[j]:
      graph[i].append(j + 1)

for key, value in graph.items():
  visited = [False] * N
  
  queue = deque(graph[key])
  
  while queue:
    currentValue = queue.popleft()
    
    if visited[currentValue - 1]: continue
        
    answer[key - 1][currentValue - 1] = 1
    visited[currentValue - 1] = True
    
    queue.extend(graph[currentValue])

for i in range(N):
  print(*answer[i])