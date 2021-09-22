import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

K = int(input())


def dfs(node, group):
    visited[node] = group

    for i in graph[node]:
        if visited[i] == 0:
            if not dfs(i, -group):
                return False
        elif visited[i] == visited[group]:
            return False

    return True


for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    flag = True
    for i in range(1, V + 1):
        if visited[i] == 0:
            flag = dfs(i, 1)

            if not flag:
                break
    print('YES' if flag else 'NO')
