import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))


LIS = []
LIS_index = []


def binary_search(arr, n):
    sp = 0
    ep = len(arr)

    while sp <= ep:
        md = (sp + ep) // 2

        if arr[md] < n:
            sp = md + 1
        else:
            ep = md - 1

    return sp


def solution():
    for num in A:
        if not LIS or LIS[-1] < num:
            LIS.append(num)
            LIS_index.append((len(LIS) - 1, num))
        else:
            res = binary_search(LIS, num)
            LIS[res] = num
            LIS_index.append((res, num))


solution()

idx = len(LIS) - 1
answer = []

for i in range(len(LIS_index) - 1, -1, -1):
    if idx == LIS_index[i][0]:
        answer.append(LIS_index[i][1])
        idx -= 1

print(len(answer))
print(*reversed(answer))
