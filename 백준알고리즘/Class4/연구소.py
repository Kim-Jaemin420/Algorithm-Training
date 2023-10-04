from collections import deque
import copy
from itertools import combinations
import sys
# input = sys.stdin.readline

sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
zeroCoordinates = []
virusCoordinates = []
answer = 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(N):
  for j in range(M):
    if graph[i][j] == 0:
      zeroCoordinates.append((i, j))
    if graph[i][j] == 2:
      virusCoordinates .append((i, j))

cases = list(combinations(zeroCoordinates, 3))

def bfs(graph):
  visited = [[False] * M for _ in range(N)]
  queue = deque(virusCoordinates)
  
  while queue:
    x, y = queue.popleft()
    visited[x][y] = True
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < N and 0 <= ny < M:
        if graph[nx][ny] == 0 and not visited[nx][ny]:
          queue.append((nx, ny))
          graph[nx][ny] = 2
  
  sum = 0
  for i in graph:
    sum += i.count(0)
  
  return sum

for case in cases:
  a, b, c = case
  safeGraph = copy.deepcopy(graph)
  safeGraph[a[0]][a[1]] = 1
  safeGraph[b[0]][b[1]] = 1
  safeGraph[c[0]][c[1]] = 1
  answer = max(answer, bfs(safeGraph))
  
print(answer)
