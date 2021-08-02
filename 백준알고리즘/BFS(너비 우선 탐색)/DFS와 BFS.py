import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    m1, m2 = map(int, input().split())
    graph[m1][m2] = graph[m2][m1] = 1


def bfs():
    visited = list()
    need_visit = list()
    need_visit.append(V)

    while need_visit:
        node = need_visit.pop(0)

        if node not in visited:
            visited.append(node)
            for i in range(N + 1):
                if graph[node][i] == 1:
                    need_visit.append(i)

    return visited


dfs_visited = [0] * (N + 1)


def dfs(n):
    dfs_visited[n] = 1
    print(n, end=' ')
    for i in range(1, N + 1):
        if dfs_visited[i] == 0 and graph[n][i] == 1:
            dfs(i)


dfs(V)
print()
print(*bfs())
