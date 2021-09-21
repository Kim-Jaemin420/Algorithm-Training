import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
A, B = map(int, input().split())
for _ in range(int(input())):
    m1, m2 = map(int, input().split())
    graph[m1].append(m2)
    graph[m2].append(m1)
visited = [0]*(N+1)


def dfs(node):
    for n in graph[node]:
        if visited[n] == 0:
            visited[n] = visited[node]+1
            dfs(n)


dfs(A)
print(visited[B] if visited[B] > 0 else -1)
