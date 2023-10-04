from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ladders, snakes = defaultdict(int), defaultdict(int)
board = [0] * 101
visited = [False] * 101
visited[1] = True

for _ in range(N):
  x, y = map(int, input().split())
  ladders[x] = y

for _ in range(M):
  u, v = map(int, input().split())
  snakes[u] = v
  
def bfs():
  queue = deque([1])
  
  while queue:
    current = queue.popleft()
    
    for i in range(1, 7):
      move = current + i
      
      if move <= 100 and not visited[move]:
        # 이동한 위치에 사다리가 있는 경우
        if ladders[move] != 0:
          move = ladders[move]
        
        # 이동한 위치에 뱀이 있는 경우
        if snakes[move] != 0:
          move = snakes[move]
          
        # 뱀 또는 사다리를 탄 결과가 아직 방문하지 않았다면
        if not visited[move]:
          board[move] = board[current] + 1
          visited[move] = True
          queue.append(move)
        
bfs()
print(board[100])