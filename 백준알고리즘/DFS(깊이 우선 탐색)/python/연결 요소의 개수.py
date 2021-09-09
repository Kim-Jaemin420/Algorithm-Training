import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
cnt = 0
visited = []

for _ in range(M):
    m1, m2 = map(int, input().split())

    graph[m1].append(m2)
    graph[m2].append(m1)


def dfs(x):
    visited.append(x)

    for i in graph[x]:
        if i not in visited:
            dfs(i)


for i in range(1, N + 1):
    if i not in visited:
        dfs(i)
        cnt += 1

print(cnt)
