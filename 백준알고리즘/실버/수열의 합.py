import sys
# input = sys.stdin.readline

sys.stdin = open('input.txt', 'r')
N, L = map(int, input().split())
M = L

while True:
  x = (N - (M - 1) * M // 2) / M
  
  if x < 0 or M > 100:
    print(-1)
    break
  
  if int(x) == x:
    print(*[i for i in range(int(x), int(x) + M)])
    break
  else:
    M += 1
