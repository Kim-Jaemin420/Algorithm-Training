import sys
input = sys.stdin.readline

N = int(input())
MOD = 15746
dp = [0] *  1000001
dp[0], dp[1] = 1, 2

for i in range(2, N + 1):
  dp[i] = (dp[i - 2] + dp[i - 1]) % MOD

print(dp[N - 1])
