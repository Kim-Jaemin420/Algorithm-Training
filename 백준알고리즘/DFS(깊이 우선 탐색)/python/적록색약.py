import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0] * N for _ in range(N)]
cnt = 0


def dfs(x, y, alpha):
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if visited[nx][ny] == 0 and graph[nx][ny] == alpha:
            dfs(nx, ny, graph[nx][ny])


for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            cnt += 1
            dfs(i, j, graph[i][j])

print(cnt, end=' ')

visited = [[0] * N for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            cnt += 1
            dfs(i, j, graph[i][j])

print(cnt)
