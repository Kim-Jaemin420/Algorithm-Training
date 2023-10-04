import sys
input = sys.stdin.readline

N = int(input())
p = [0] + list(map(int, input().split()))

dp = [0] * (N + 1)

for i in range(1, N + 1):
  for j in range(1, i + 1):
    dp[i] = max(p[j] + dp[i - j], dp[i])

print(max(dp))