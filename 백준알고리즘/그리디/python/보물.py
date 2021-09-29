import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
C = sorted(B)
res = 0

for i in range(N):
  res += A[i] * C[i]
print(res)