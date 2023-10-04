from collections import deque
import sys
# input = sys.stdin.readline

sys.stdin = open('input.txt', 'r')

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
count = 0
ROW = 0
COLUMN = 1
DIAGONAL = 2

def dfs(x, y, direction):
  global count
  
  if x == N - 1 and y == N - 1:
    count += 1
    return
  
  if x + 1 < N and y + 1 < N:
      # 대각선으로 이동
    if graph[x + 1][y + 1] == 0 and graph[x][y + 1] == 0 and graph[x + 1][y] == 0:
      dfs(x + 1, y + 1, DIAGONAL)
      
  if direction == ROW or direction == DIAGONAL:
    # 세로로 이동
    if x + 1 < N:
      if graph[x + 1][y] == 0:
        dfs(x + 1, y, ROW)
  
  if direction == COLUMN or direction == DIAGONAL:
    # 가로로 이동
    if y + 1 < N:
      if graph[x][y + 1] == 0:
        dfs(x, y + 1, COLUMN)
  
 

dfs(0, 1, COLUMN)

print(count)