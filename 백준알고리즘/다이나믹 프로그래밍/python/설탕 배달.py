import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (N // 3 + 1)

for i in range(len(dp)):
  if (N - (i + 1) * 3) % 5 == 0:
    dp[i] = (i + 1) + (N - (i + 1) * 3) // 5
    
dp = [number for number in dp if number != 0]

print(min(dp) if dp else -1)