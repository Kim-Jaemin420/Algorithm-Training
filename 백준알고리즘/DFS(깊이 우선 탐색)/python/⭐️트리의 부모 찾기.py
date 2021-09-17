import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
parents = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    m1, m2 = map(int, input().split(' '))
    graph[m1].append(m2)
    graph[m2].append(m1)


def dfs(x, parents):
    for num in graph[x]:
        if parents[num] == 0:
            parents[num] = x
            dfs(num, parents)


dfs(1, parents)
for v in parents[2:]:
    print(v)
