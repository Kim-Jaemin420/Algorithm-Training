import sys
# input = sys.stdin.readline

sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
size = 1

for i in range(N):
  for j in range(M):
    number = graph[i][j]
    
    for k in range(min(N, M) - 1, 0, -1):
      if k >= M - j or k >= N - i:
        continue
      if graph[i][j + k] != number or graph[i + k][j] != number or graph[i + k][j + k] != number:
        continue
      if graph[i][j + k] == number or graph[i + k][j] == number or graph[i + k][j + k] == number:
        size = max(size, (k + 1) ** 2)
      
print(size)

  