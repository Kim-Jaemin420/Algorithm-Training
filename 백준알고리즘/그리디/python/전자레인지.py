import sys
input = sys.stdin.readline

T = int(input())
A, B, C = 5*60, 60, 10
timer = [300, 60, 10]
cnt = [0, 0, 0]

for i in range(3):
  if T >= timer[i]:
    cnt[i] = T // timer[i]
    T -= timer[i] * (T // timer[i])

print(*cnt) if T == 0 else print(-1)