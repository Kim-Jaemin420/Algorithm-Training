import sys
input = sys.stdin.readline

N = int(input())
lines = list(map(int, input().split()))
LIS = []


def binary_search(arr, line):
    sp = 0
    ep = len(arr) - 1

    while sp <= ep:
        md = (sp + ep) // 2

        if arr[md] < line:
            sp = md + 1
        else:
            ep = md - 1
    return sp


for line in lines:
    if not LIS or LIS[-1] < line:
        LIS.append(line)
    else:
        res = binary_search(LIS, line)
        LIS[res] = line


print(N - len(LIS))
