import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(input()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
answer = []


def dfs(x, y):
    global cnt
    cnt += 1
    matrix[x][y] = '0'

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if matrix[nx][ny] == '1':
            dfs(nx, ny)


for i in range(N):
    for j in range(N):
        if matrix[i][j] == '1':
            cnt = 0
            dfs(i, j)
            answer.append(cnt)

print(len(answer))
answer.sort()
for item in answer:
    print(item)
