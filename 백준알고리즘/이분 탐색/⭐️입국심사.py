import sys
input = sys.stdin.readline

N, M = map(int, input().split())

total_time = [int(input()) for _ in range(N)]

sp = min(total_time)
ep = max(total_time) * M

ans = float('inf')

while sp <= ep:
    md = (sp + ep) // 2
    people_per_time = 0

    for t in total_time:
        people_per_time += md // t

    if people_per_time < M:
        sp = md + 1
    else:
        ans = min(ans, md)
        ep = md - 1
print(ans)
