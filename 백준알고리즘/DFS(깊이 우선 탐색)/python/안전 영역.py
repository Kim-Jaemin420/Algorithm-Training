import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * N for _ in range(N)]
answer = {}
cnt = 0


for _ in range(N):
    graph.append(list(map(int, input().split())))
M = max(map(max, graph))


def dfs(x, y, n):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if graph[nx][ny] > n and visited[nx][ny] == False:
            dfs(nx, ny, n)


def solution():
    global cnt, visited
    for n in range(0, M + 1):
        for i in range(N):
            for j in range(N):
                if graph[i][j] > n and visited[i][j] == False:
                    cnt += 1
                    dfs(i, j, n)
        visited = [[False] * N for _ in range(N)]
        answer[n] = cnt
        cnt = 0


solution()
print(max(answer.values()))
