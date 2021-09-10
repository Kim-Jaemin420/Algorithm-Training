import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

w, h = map(int, input().split())
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]
cnt = 0


def dfs(x, y, graph):
    graph[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue

        if graph[nx][ny] == 1:
            dfs(nx, ny, graph)


def solution(w, h, graph):
    global cnt
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                cnt += 1
                dfs(i, j, graph)

    return cnt


while w != 0 and h != 0:
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    print(solution(w, h, graph))
    graph = []
    w, h = map(int, input().split())
    cnt = 0
