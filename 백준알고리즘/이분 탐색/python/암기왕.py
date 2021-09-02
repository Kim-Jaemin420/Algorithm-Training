import sys
input = sys.stdin.readline

T = int(input())


def solution():
    N = int(input())
    note1 = list(map(int, input().split()))
    M = int(input())
    note2 = list(map(int, input().split()))
    ans = []

    note1.sort()

    for n in note2:
        sp = 0
        ep = N - 1
        while sp <= ep:
            md = (sp + ep) // 2

            if note1[md] < n:
                sp = md + 1
            elif note1[md] > n:
                ep = md - 1
            else:
                ans.append(1)
                break
        if note1[md] != n:
            ans.append(0)
    return ans


for _ in range(T):
    for i in solution():
        print(i)
