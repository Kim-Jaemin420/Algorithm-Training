import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = [int(input()) for _ in range(0, N)]

house.sort()


def count(d):
    cnt = 1
    ep = house[0]

    for i in range(1, N):
        if house[i] - ep >= d:
            cnt += 1
            ep = house[i]
    return cnt


def install_router():
    answer = 0
    sp = 1
    ep = house[-1] - house[0]

    while sp <= ep:
        md = (sp + ep) // 2
        if count(md) >= C:
            answer = md
            sp = md + 1
        else:
            ep = md - 1

    return answer


print(install_router())
