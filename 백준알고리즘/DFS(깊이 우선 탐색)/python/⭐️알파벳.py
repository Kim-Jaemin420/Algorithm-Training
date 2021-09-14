import sys
input = sys.stdin.readline


R, C = map(int, input().split(' '))
graph = [list(map(lambda x: ord(x) - 65, input().rstrip())) for _ in range(R)]

visited = [0] * 26
visited[graph[0][0]] = 1
answer = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, ans):
    global answer

    answer = max(ans, answer)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if visited[graph[nx][ny]] == 0:
            visited[graph[nx][ny]] = 1
            dfs(nx, ny, ans + 1)
            visited[graph[nx][ny]] = 0


dfs(0, 0, answer)
print(answer)
