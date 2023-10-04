from collections import deque
import sys
# input = sys.stdin.readline

sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
dp = [0] * (K + 2)
visited = [0] * 100001

queue = deque()
queue.append(N)

time = 0
way = 0

while queue:
  current = queue.popleft()
  count = visited[current]
  
  if current == K:
    time = visited[current]
    way += 1
    continue
  
  for nx in [current - 1, current + 1, current * 2]:
    if  0 <= nx < 100001:
      if visited[nx] == 0 or visited[nx] == visited[current] + 1:
        queue.append(nx)
        visited[nx] = count + 1
        
print(time)
print(way)