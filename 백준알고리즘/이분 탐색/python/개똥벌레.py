import sys
input = sys.stdin.readline

N, H = map(int, input().split())
top, bottom, obstacles = [], [], []

for i in range(N):
    if i % 2 == 0:
        bottom.append(int(input()))
    else:
        top.append(int(input()))

for i in range(1, H + 1):
    cnt = 0
    for j in range(N // 2):
        if top[j] > H - i:
            cnt += 1
        if bottom[j] >= i:
            cnt += 1
    obstacles.append(cnt)

print(min(obstacles), obstacles.count(min(obstacles)))
