from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
boxes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
dx, dy, dz = [-1, 1, 0, 0, 0, 0], [0, 0, 0, 0, -1, 1], [0, 0, -1, 1, 0, 0]
visited = [[[False] * M for _ in range(N)] for _ in range(H)]
queue = deque()

def bfs():
  while queue:
    x, y, z = queue.popleft()
    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nz = z + dz[i]

      if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M:
        if boxes[nx][ny][nz] == 0:
          boxes[nx][ny][nz] = boxes[x][y][z] + 1
          queue.append((nx, ny, nz))
          

for i in range(H):
  for j in range(N):
    for k in range(M):
      if boxes[i][j][k] == 1:
        queue.append((i, j, k))

bfs()

takenDate = -1
for box in boxes:
  for tomatoes in box:
    for tomato in tomatoes:
      if tomato == 0:
        print(-1)
        exit(0)
    takenDate = max(takenDate, max(tomatoes))

print(takenDate - 1)