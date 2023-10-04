from collections import deque
import sys
input = sys.stdin.readline

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
N = int(input())
aquarium = [list(map(int, input().split())) for _ in range(N)]
sharkX, sharkY, sharkSize = 0, 0, 2
SHARK_NUMBER = 9
time = 0
eatenFishNumber = 0

for i in range(N):
  for j in range(N):
    if aquarium[i][j] == SHARK_NUMBER:
      sharkX, sharkY = i, j
      aquarium[sharkX][sharkY] = 0
      break

def eatFish(sharkX, sharkY):
  willEatFishes = []
  distance = [[0] * N for _ in range(N)]
  visited = [[False] * N for _ in range(N)]
  queue = deque()
  queue.append((sharkX, sharkY))
  
  while queue:
    currentX, currentY = queue.popleft()
    
    for i in range(4):
      nx = currentX + dx[i]
      ny = currentY + dy[i]
      
      if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
        if aquarium[nx][ny] <= sharkSize:
          queue.append((nx, ny))
          distance[nx][ny] = distance[currentX][currentY] + 1
          visited[nx][ny] = True
          if aquarium[nx][ny] < sharkSize and aquarium[nx][ny] != 0:
            willEatFishes.append((nx, ny, distance[nx][ny]))
  
  return sorted(willEatFishes, key=lambda x: (-x[2], -x[1], -x[0]))


while True:
  sortedWillEatFishes = eatFish(sharkX, sharkY)
  
  if not sortedWillEatFishes:
    break
  
  x, y, distance = sortedWillEatFishes.pop()
  
  if aquarium[x][y] < sharkSize:
    eatenFishNumber += 1
    time += distance
    aquarium[sharkX][sharkY], aquarium[x][y] = 0, 0
    sharkX, sharkY = x, y
  
  if eatenFishNumber == sharkSize:
    sharkSize += 1
    eatenFishNumber = 0
  
print(time)
