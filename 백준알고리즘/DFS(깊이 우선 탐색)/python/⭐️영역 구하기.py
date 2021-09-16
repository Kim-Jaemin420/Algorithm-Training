import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

M, N, K = map(int, input().split(' '))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = []
cnt = 0
graph = [[0] * N for _ in range(M)]

for _ in range(K):
    m1, k1, m2, k2 = map(int, input().split())
    for q in range(m1, m2):
        for p in range(k1, k2):
            graph[p][q] = -1


def dfs(x, y):
    global cnt
    graph[x][y] = 1
    cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
        if graph[nx][ny] == 0:
            dfs(nx, ny)


for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            cnt = 0
            dfs(i, j)
            ans.append(cnt)

ans.sort()
print(len(ans))
print(*ans)
