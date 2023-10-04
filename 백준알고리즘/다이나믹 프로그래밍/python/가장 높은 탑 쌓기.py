import sys
input = sys.stdin.readline

N = int(input())
bricks = [(0, 0, 0, 0)]
dp = [0] * (N + 1)

for index in range(1, N + 1):
  area, height, weight = map(int, input().split())
  bricks.append((index, area, height, weight))

bricks.sort(key=lambda x: x[3])


for i in range(1, N + 1):
  for j in range(0, i):
    if bricks[i][1] > bricks[j][1]:
      dp[i] = max(dp[i], dp[j] + bricks[i][2])

max_value = max(dp)
index = N
result = []

while index != 0:
  if max_value == dp[index]:
    result.append(bricks[index][0])
    max_value -= bricks[index][2]
    
  index -= 1

result.reverse()
print(len(result))
[print(result[i]) for i in range(len(result))]