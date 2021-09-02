import sys
input = sys.stdin.readline

N = int(input())
solution_list = list(map(int, input().split()))

solution_list.sort()


def binary_search(num, idx):
    sp = idx + 1
    ep = N - 1
    min_v = float('inf')
    ans = []

    while sp < ep:
        res = num + solution_list[sp] + solution_list[ep]
        if sp == ep:
            break

        if abs(res) <= min_v:
            ans = [num, solution_list[sp], solution_list[ep]]
            min_v = abs(res)
        if res >= 0:
            ep -= 1
        else:
            sp += 1
    return min_v, ans


def solution():
    min_v = float('inf')
    ans = []
    for i in range(N):
        res = binary_search(solution_list[i], i)
        if min_v >= res[0]:
            min_v = res[0]
            ans = res[1]

    return ans


print(*solution())
