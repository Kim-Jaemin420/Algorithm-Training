N, K = int(input()), int(input())
sp, ep = 1, K

while sp <= ep:
    md = (sp + ep) // 2

    cnt = 0
    for i in range(1, N+1):
        cnt += min(md // i, N)

    if cnt >= K:
        answer = md
        ep = md - 1
    else:
        sp = md + 1

print(answer)
