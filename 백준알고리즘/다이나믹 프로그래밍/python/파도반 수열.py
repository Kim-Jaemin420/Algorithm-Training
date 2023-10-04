import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N = int(input())
  dp = [0] * N
  dp[0] = 1
  
  if N > 1:
    dp[1] = 1
  if N > 2:
    dp[2] = 1
  
  for i in range(3, N):
    dp[i] = dp[i - 3] + dp[i - 2]
  
  print(dp[N - 1])