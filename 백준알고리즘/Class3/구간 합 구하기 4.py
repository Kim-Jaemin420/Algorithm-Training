import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]

sum_value = 0
for number in numbers:
  sum_value += number
  prefix_sum.append(sum_value)

for _ in range(M):
  i, j = map(int, input().split())
  print(prefix_sum[j] - prefix_sum[i - 1])