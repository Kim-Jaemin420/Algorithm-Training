import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent, child = 1, 1

for i in range(n, n - m, -1):
  parent *= i

for i in range(1, m + 1):
  child *= i

print(parent // child)