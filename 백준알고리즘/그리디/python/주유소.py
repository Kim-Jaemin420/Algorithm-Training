import sys
input = sys.stdin.readline

N = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))
res = 0

p = prices[0]
for i in range(1, N):
  res += p * distances[i - 1]
  if prices[i] < p:
    p = prices[i]
  
  
print(res)