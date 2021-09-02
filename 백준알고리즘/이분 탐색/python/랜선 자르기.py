import sys
input = sys.stdin.readline

K, N = map(int, input().split())
cable_list = []

for i in range(K):
    cable_list.append(int(input()))

cable_list.sort()


def cut_cable():
    sp = 0
    ep = cable_list[-1]
    while sp <= ep:
        cnt = 0
        md = 1 if (sp + ep) // 2 == 0 else (sp + ep) // 2

        for cable in cable_list:
            cnt += cable // md

        if cnt < N:
            ep = md - 1
        else:
            sp = md + 1
    if cnt >= N:
        return md
    while cnt < N:
        cnt = 0
        md -= 1
        for cable in cable_list:
            cnt += cable // md
        return md


print(cut_cable())
