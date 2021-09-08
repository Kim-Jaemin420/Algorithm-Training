import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0


def solution():
    M, N, K = map(int, input().split())
    global cnt
    graph = [[0] * N for _ in range(M)]

    for _ in range(K):
        m1, m2 = map(int, input().split())
        graph[m1][m2] = 1

    def dfs(x, y):
        graph[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1:
                dfs(nx, ny)

    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                cnt += 1
                dfs(i, j)

    return cnt


for _ in range(int(input())):
    cnt = 0
    print(solution())
