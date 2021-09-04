from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(input()) for _ in range(N)]

visited = [[0] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

total = []
total_cnt = 0


def bfs(x, y, idx):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and matrix[nx][ny] == '1':
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    apt_list[idx] += 1


apt_list = {}
idx = 0
for i in range(N):
    for j in range(N):
        if matrix[i][j] == '1' and visited[i][j] == 0:
            apt_list[idx] = 1
            bfs(i, j, idx)
            idx += 1

apt_list = sorted(apt_list.values())
print(len(apt_list))
for i in apt_list:
    print(i)
