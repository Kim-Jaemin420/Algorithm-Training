import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

LIS_index = []
LIS = []


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


for i in range(len(A)):
    if not LIS or LIS[-1] < A[i]:
        LIS.append(A[i])
        LIS_index.append((len(LIS) - 1, A[i]))
    else:
        res = binary_search(LIS, A[i])
        LIS_index.append((res, A[i]))

answer = []
idx = len(LIS) - 1

for i in range(len(LIS_index) - 1, -1, -1):
    if idx == LIS_index[i][0]:
        print(LIS_index[i][1])
        answer.append(LIS_index[i][1])
        idx -= 1

print(LIS_index)
print(len(answer))
print(*answer[::-1])
