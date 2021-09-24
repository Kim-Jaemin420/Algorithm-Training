import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []

for _ in range(N):
    coins.append(int(input()))

coins.sort(reverse=True)
cnt = 0
target = K

for i in range(N):
    if target >= coins[i]:
        cnt += target // coins[i]
        target -= coins[i] * (target // coins[i])
print(cnt)
