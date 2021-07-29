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

####################################
# 2회차 풀이
####################################
input = sys.stdin.readline

N, M = map(int, input().split())
times = [int(input()) for _ in range(N)]

sp = min(times)
ep = max(times) * M

answer = 0
while sp <= ep:
    md = (sp + ep) // 2

    total = 0
    for time in times:
        total += md // time

    if total < M:
        sp = md + 1
    else:
        answer = md
        ep = md - 1

print(answer)
