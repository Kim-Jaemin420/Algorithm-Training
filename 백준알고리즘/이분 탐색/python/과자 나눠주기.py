import sys
input = sys.stdin.readline

M, N = map(int, input().split())
snacks = list(map(int, input().split()))

sp = 1
ep = max(snacks)
res = 0


def devide(n):
    cnt = 0
    for snack in snacks:
        cnt += snack // n

    return cnt


while sp <= ep:
    md = (sp + ep) // 2

    if devide(md) >= M:
        sp = md + 1
        res = md
    else:
        ep = md - 1

print(res)
