import sys
input = sys.stdin.readline

N = int(input())
p = list(map(int, input().split()))
p.sort()

cnt = 0

for i in range(N):
    cnt += p[i] * (N - i)
print(cnt)
