from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
ripedTomatoes = deque()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(N):
  for j in range(M):
    if graph[i][j] == 1:
      ripedTomatoes.append([i, j])

def ripingTomatoes():
  while ripedTomatoes:
    x, y = ripedTomatoes.popleft()
    
    for i in range(4):
      nx, ny = dx[i] + x, dy[i] + y
      if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
        graph[nx][ny] = graph[x][y] + 1
        ripedTomatoes.append([nx, ny])

ripingTomatoes()

answer = 0

for tomatoes in graph:
  for tomato in tomatoes:
    if tomato == 0:
      print(-1)
      exit(0)
  answer = max(answer, max(tomatoes))

print(answer - 1)
    
