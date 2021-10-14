import sys
input = sys.stdin.readline

N = int(input())

dp = [0, 1, 1]

def solution(n):
  length = len(dp)
  if n > 2:
    for i in range(length, N + 1):
      dp.append(dp[i - 2] + dp[i - 1])

solution(N)
print(dp[N])