import sys
input = sys.stdin.readline

remain = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]
ans = 0

for coin in coins:
    if coin <= remain:
        ans += remain // coin
        remain -= coin * (remain // coin)

print(ans)
