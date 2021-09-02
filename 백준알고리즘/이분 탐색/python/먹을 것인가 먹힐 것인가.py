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
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0

    B.sort()

    for a in A:
        res = binary_search(B, a)
        cnt += res

    return cnt


for _ in range(int(input())):
    print(solution())
