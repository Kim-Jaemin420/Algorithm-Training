import sys
input = sys.stdin.readline

M, N = int(input()), int(input())


def find_decimal(num):
    if num == 2:
        return 1
    elif num == 1 or num % 2 == 0:
        return 0
    else:
        for i in range(2, num):
            if num % i == 0:
                return 0
    return 1


decimals = []


def decimal_sum_min():
    for num in range(M, N + 1):
        if find_decimal(num) == 1:
            decimals.append(num)
    if len(decimals) == 0:
        return -1
    else:
        return decimals


res = decimal_sum_min()
if res == -1:
    print(-1)
else:
    print(sum(res))
    print(res[0])
