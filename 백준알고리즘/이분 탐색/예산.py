import sys
input = sys.stdin.readline

N = int(input())
province = list(map(int, input().split()))
M = int(input())


def counter(m):
    total = 0

    for p in province:
        if p <= m:
            total += p
        else:
            total += m

    return total


def allocate_budget():
    answer = 0
    sp = 0
    ep = max(province)

    while sp <= ep:
        md = (sp + ep) // 2

        if counter(md) <= M:
            answer = md
            sp = md + 1
        else:
            ep = md - 1

    return answer


print(allocate_budget())
