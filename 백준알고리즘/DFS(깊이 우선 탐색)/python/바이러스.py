import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    m1, m2 = map(int, input().split())
    graph[m1][m2] = graph[m2][m1] = 1

visited = [0 for _ in range(N + 1)]


def dfs(n):
    visited[n] = 1

    for i in range(N + 1):
        if graph[n][i] == 1 and visited[i] == 0:
            dfs(i)


dfs(1)

cnt = 0
for i in visited:
    if i == 1:
        cnt += 1
print(cnt - 1)
