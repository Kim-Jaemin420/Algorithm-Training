import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
rests = list(map(int, input().split()))

rests.append(0)
rests.append(L - 1)
rests = sorted(rests)

sp = 0
ep = L - 1

while sp <= ep:
    md = (sp + ep) // 2
    cnt = 0
    for i in range(0, N + 1):
        if rests[i + 1] - rests[i] > md:
            cnt += (rests[i + 1] - rests[i] - 1) // md

    if cnt > M:
        sp = md + 1
    else:
        answer = md
        ep = md - 1

print(answer)
