import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

I, J = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[-1] * J for _ in range(I)]

for _ in range(I):
    m = list(map(int, input().split()))
    graph.append(m)


def dfs(x, y):
    if x == I - 1 and y == J - 1:
        return 1
    if visited[x][y] != -1:
        return visited[x][y]

    visited[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= I or ny < 0 or ny >= J:
            continue

        if graph[nx][ny] < graph[x][y]:
            visited[x][y] += dfs(nx, ny)
    return visited[x][y]


print(dfs(0, 0))
