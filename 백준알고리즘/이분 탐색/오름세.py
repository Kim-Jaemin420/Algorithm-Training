import sys
input = sys.stdin.readline


def binary_search(arr, num):
    sp = 0
    ep = len(arr) - 1

    while sp <= ep:
        md = (sp + ep) // 2

        if arr[md] < num:
            sp = md + 1
        else:
            ep = md - 1

    return sp


def solution():
    p_list = list(map(int, input().split()))
    LIS = []

    for p in p_list:
        if not LIS or LIS[-1] < p:
            LIS.append(p)
        else:
            res = binary_search(LIS, p)
            LIS[res] = p
    return len(LIS)


while input():
    print(solution())
