import sys
input = sys.stdin.readline


def binary_search(list, val):
    sp, ep = 0, len(list) - 1

    while sp <= ep:
        md = (sp + ep) // 2

        if list[md] > val:
            ep = md - 1
        else:
            sp = md + 1

    return sp


n = int(input())
semi_list = list(map(int, input().split()))
D = []

for semi in semi_list:
    if not D or D[-1] < semi:
        D.append(semi)
    else:
        D[binary_search(D, semi)] = semi

print(len(D))
