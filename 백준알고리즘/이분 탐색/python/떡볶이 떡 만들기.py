import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tteoks = list(map(int, input().split()))

sp = 0
ep = max(tteoks)

while sp <= ep:
    md = (sp + ep) // 2
    total = 0

    for t in tteoks:
        if t > md:
            total += t - md

    if total > M:
        sp = md + 1
    else:
        ep = md - 1

print(sp)
