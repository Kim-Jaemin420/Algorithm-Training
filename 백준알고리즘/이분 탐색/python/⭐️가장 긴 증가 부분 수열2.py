import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))

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
    for num in num_list:
        if not LIS or LIS[-1] < num:
            LIS.append(num)
        else:
            res = binary_search(LIS, num)
            LIS[res] = num or 0


solution()
print(len(LIS))

####################################
# 2회차 풀이
####################################
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

LIS = []


def binary_search(n, arr):
    sp = 0
    ep = len(arr) - 1

    while sp <= ep:
        md = (sp + ep) // 2

        if arr[md] < n:
            sp = md + 1
        else:
            ep = md - 1
    return sp


for n in arr:
    if not LIS or n > LIS[-1]:
        LIS.append(n)
    else:
        res = binary_search(n, LIS)
        LIS[res] = n

print(len(LIS))
