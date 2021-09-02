import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
LIS = []


def binary_search(LIS, n):
    sp = 0
    ep = len(LIS) - 1

    while sp <= ep:
        md = (sp + ep) // 2

        if LIS[md] < n:
            sp = md + 1
        else:
            ep = md - 1

    return sp


def solution():
    for num in A:
        if not LIS or LIS[-1] < num:
            LIS.append(num)
        else:
            res = binary_search(LIS, num)
            LIS[res] = num


solution()
print(len(LIS))
