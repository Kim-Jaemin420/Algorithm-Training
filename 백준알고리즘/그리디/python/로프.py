import sys
input = sys.stdin.readline

N = int(input())
ropes = [int(input()) for _ in range(N)]

ropes.sort()
ans = []


for i in range(N):
    ans.append(ropes[i] * (N - i))
print(max(ans))
