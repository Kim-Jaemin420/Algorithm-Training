import sys
input = sys.stdin.readline

N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * N

for i in range(N - 1):
  date = i
  j = i
  price = 0
  
  while j < N - 1:
    if j == N - 1 and schedule[j][0] > 1 or j > N - 1:
      break
    price += schedule[j][1]
    j += schedule[j - 1][0]
    print(i, j, price)
    
  
  dp[i] = price

print(dp)
print(max(dp))