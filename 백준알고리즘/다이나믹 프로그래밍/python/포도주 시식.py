import sys
input = sys.stdin.readline

n = int(input())
wines = [int(input()) for _ in range(n)]
dp = [wines[0]]

if n > 1:
  dp.append(wines[0] + wines[1])
  
if n > 2:
  dp.append(max(wines[1] + wines[2], wines[0] + wines[2], dp[1], dp[0]))

for i in range(3, n):
  dp.append(max(wines[i] + dp[i - 3] + wines[i - 1], wines[i] + dp[i - 2], dp[i - 1]))

print(max(dp))