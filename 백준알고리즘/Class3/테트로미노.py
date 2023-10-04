import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
cases = [
  [(0, 0), (0, 1), (1, 0), (1, 1)], 
  [(0, 0), (0, 1), (0, 2), (0, 3)], 
  [(0, 0), (1, 0), (2, 0), (3, 0)], 
  [(0, 0), (1, 0), (1, 1), (2, 1)], 
  [(0, 0), (1, 0), (1, -1), (2, -1)], 
  [(0, 0), (0, 1), (1, 1), (1, 2)], 
  [(0, 0), (0, 1), (-1, 1), (-1, 2)], 
  [(0, 0), (0, 1), (0, 2), (1, 2)], 
  [(0, 0), (1, 0), (2, 0), (2, -1)], 
  [(0, 0), (1, 0), (1, 1), (1, 2)], 
  [(0, 0), (0, -1), (1, -1), (2, -1)], 
  [(0, 0), (-1, 0), (-1, 1), (-1, 2)], 
  [(0, 0), (1, 0), (2, 0), (2, 1)], 
  [(0, 0), (0, 1), (0, 2), (-1, 2)], 
  [(0, 0), (0, 1), (1, 1), (2, 1)], 
  [(0, 0), (0, 1), (-1, 1), (0, 2)], 
  [(0, 0), (1, 0), (1, 1), (2, 0)], 
  [(0, 0), (0, 1), (1, 1), (0, 2)], 
  [(0, 0), (1, 0), (1, -1), (2, 0)]
]

maxValue = 0  

for i in range(N):
  for j in range(M):
    for case in cases:
      temp = 0
      for coordinate in case:
        if 0 <= i + coordinate[0] < N and 0 <= j + coordinate[1] < M:
          temp += graph[i + coordinate[0]][j + coordinate[1]]
      maxValue = max(temp, maxValue)
      
print(maxValue)