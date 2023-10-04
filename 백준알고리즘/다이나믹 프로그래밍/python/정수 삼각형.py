import sys
input = sys.stdin.readline

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
  for j in range(i + 1):
    if j == 0:
      nums[i][j] = nums[i][j] + nums[i - 1][j]
    elif i == j:
      nums[i][j] = nums[i][j] + nums[i - 1][j - 1]
    else:
      nums[i][j] = max(nums[i][j] + nums[i - 1][j - 1], nums[i][j] + nums[i - 1][j])
      
print(max(nums[-1]))